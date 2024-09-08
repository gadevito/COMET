
import pandas as pd

import itertools

#import talos as ta

from gensim.models import KeyedVectors

from helpers import create_embedding_matrix, tokens2index, texts2index_padded, prune_wv

import numpy as np
import time
import gc

from keras.models import Model
from keras.optimizers import Adam, Nadam
from keras.layers import TimeDistributed, GlobalMaxPooling1D, GlobalAveragePooling1D, Activation, Input, LSTM, GRU, Dense, Dropout, Flatten, Embedding, SpatialDropout1D, Bidirectional, CuDNNGRU
from keras.layers.convolutional import Conv1D, MaxPooling1D, AveragePooling1D
from keras.layers.normalization import BatchNormalization
from keras.layers import Flatten, concatenate
from keras.engine.topology import Layer
from keras import initializers, regularizers, constraints, activations
from keras.layers.recurrent import Recurrent
from keras.engine import InputSpec
from keras.callbacks import ModelCheckpoint, EarlyStopping, LearningRateScheduler, ReduceLROnPlateau, CSVLogger
from keras.wrappers.scikit_learn import KerasRegressor

import spacy
from spacy.symbols import ORTH, LEMMA, POS, TAG, LOWER

from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, mean_absolute_error

import tensorflow as tf
from tensorflow import set_random_seed
from keras import backend as K

random_seed = 102329
use_cases_df = pd.read_csv("use-cases.csv", index_col=0)

tokenized_names = [name.split(" ") for name in use_cases_df['TitleTokens'].tolist()]

train_ids = pd.read_csv("10-fold-train-full.csv", index_col=0)
val_ids = pd.read_csv("10-fold-val-full.csv", index_col=0)

runs = train_ids.run.max() + 1 
k = train_ids.k.max() + 1

"""
use_cases = [
"Access the 'Threshold List' section",
"Insert threshold",
"Display threshold details",
"Update threshold",
"Delete a threshold",
"Measurements taken",
"Display measurement graphs",
"View Alert",
"Record the exit of the patient from the security area",
"Patient’s steps count",
"Record the patient's heartbeat",
"Insert a patient’s fall event",
"Record the number of calls following the press of the \"SOS\" button"]
"""

use_cases = [
"Record the number of calls following the press of the \"SOS\" button"]


start_time = time.perf_counter()
nlp = spacy.load('en_core_web_lg')

stop_words = spacy.lang.en.stop_words.STOP_WORDS
filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n'

titles = []
for text in use_cases:
    doc = nlp(text)
    tokens = " ".join([token.lower_ for token in doc if not token.orth_.isspace() and not token.orth_ in filters and not token.orth_ in stop_words])
    titles.append(tokens)

tokenized_pred_names = [name.split(" ") for name in titles]

tokenized_all_names = tokenized_pred_names + tokenized_names

end_time = time.perf_counter()

duration = end_time - start_time

def get_deep_cosmic_uc_model():
        
    global MAX_SEQUENCE_LENGTH, embedding_matrix

    embedding_layer = Embedding(input_dim=embedding_matrix.shape[0],
                 output_dim=embedding_matrix.shape[1],
                 mask_zero=False,
                 weights=[embedding_matrix],
                 input_length=MAX_SEQUENCE_LENGTH,
                 trainable=False)

    line_input = Input(shape=(MAX_SEQUENCE_LENGTH,), dtype='int32', name="input")
    embedded_sequences = embedding_layer(line_input)
    cnn = Conv1D(filters=10, kernel_size=2, strides=1, 
                        padding='same', activation='relu')(embedded_sequences)
    cnn = MaxPooling1D(pool_size=2)(cnn)
    cnn = Conv1D(filters=12, kernel_size=2, strides=1, 
                        padding='same', activation='relu')(cnn)
    cnn = MaxPooling1D(pool_size=2)(cnn)
    cnn = Dropout(0.5)(cnn)
    cnn = GlobalAveragePooling1D()(cnn)

    output = Dense(1, activation='linear')(cnn)

    model = Model([line_input] , output)
    algorithm = Adam(lr=0.001, beta_1=0.95, beta_2=0.999, epsilon=1e-08, decay=0.0) #0.005

    model.compile(optimizer=algorithm, loss='mae', metrics=['mse','mae'])

    return model


wv = KeyedVectors.load_word2vec_format("w2v_glove.6B.300d.word2vec.txt", binary=False)

wv = prune_wv(wv, tokenized_all_names)
MAX_SEQUENCE_LENGTH, VECTOR_LENGTH = 16, wv.vector_size
embedding_matrix = create_embedding_matrix(wv, VECTOR_LENGTH)
embedding_matrix.shape
gc.collect()

start_time = time.perf_counter()
x = texts2index_padded(tokenized_names, wv, seq_length=MAX_SEQUENCE_LENGTH)
y = use_cases_df['Cfp']

get_deep_cosmic_uc_model().summary()

np.random.seed(random_seed)
set_random_seed(random_seed)

callbacks_list = [
    ReduceLROnPlateau( 
        monitor='loss',
        min_lr=0.001, 
        factor=0.5,
        verbose=1,
        patience=10) 
]

estimators = []
estimators.append(('cnn', KerasRegressor(build_fn=get_deep_cosmic_uc_model, epochs=400,
                                        batch_size=200, verbose=2, callbacks=callbacks_list))) 

model = Pipeline(estimators)

model.fit(x, y)


x_pred = texts2index_padded(tokenized_pred_names, wv, seq_length=MAX_SEQUENCE_LENGTH)

y_pred = model.predict(x_pred)

predictions = pd.DataFrame({'use case':use_cases, 'Cfp-pred':y_pred, 'Cfp-int':np.round(y_pred)})

end_time = time.perf_counter()

duration += end_time - start_time
print(predictions)

print("TOTAL TIME:", duration)