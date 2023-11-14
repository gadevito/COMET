import sklearn
import openai
from sklearn.model_selection import GridSearchCV
from sklearn.base import BaseEstimator
from rouge import Rouge
#import logging
import os
#import sys
import loggersp, logging
from prompt import *
import time


class COMETSPLIT(BaseEstimator):

    def __init__(self, temperature=0.5, max_tokens =1100, model ="gpt-4", top_p = 1, presence_penalty = 0.0, frequency_penalty= 0.0):
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.model = model
        self.top_p = top_p
        self.presence_penalty =presence_penalty
        self.frequency_penalty = frequency_penalty
        self.rouge = Rouge()


    def fit(self, x, y, w=None):
        return self

    def predict(self, X):
        # Genera il testo utilizzando GPT-4
        responses = []
        api_key = os.getenv('OPENAI_KEY')
        openai.api_key = api_key
        timeout = 5
        for text in X:
            while True:
                try:
                    response = openai.ChatCompletion.create(
                        model=self.model,
                        messages=[
                            {"role": "system", "content": SYSTEM_SPLIT_UC},
                            {"role": "user", "content": text+"\nSplit:"}
                        ],
                        temperature=self.temperature, 
                        frequency_penalty=self.frequency_penalty, 
                        presence_penalty=self.presence_penalty
                    )
                    responses.append(response['choices'][0]['message']['content'])
                    timeout = 5
                    break
                except Exception as e:
                    time.sleep(timeout)
                    timeout = timeout *2

        return responses
    
    def score(self, X, y):
        y_pred = self.predict(X)

        print("CALCOLO", y_pred, y)
        scores = self.rouge.get_scores(y_pred, y, avg=True)

        r1 = scores['rouge-1']
        print("ROUGE ==>", r1)
        conf = str(self.get_params(self))
        score = str(r1['f'])
        _logger = loggersp._logger #.getLogger("COSMIC_ANALYSIS")
        _logger.debug("testing "+conf+" score "+score)
        #_logger.debug("generated:\n"+y_pred)
        #_logger.debug("labeled value:\n"+y)
        return r1['f']

    def get_params(self, deep=True):
        return {"temperature": self.temperature, 
                "max_tokens": self.max_tokens,
                "model": self.model,
                "top_p": self.top_p,
                "frequency_penalty": self.frequency_penalty,
                "presence_penalty": self.presence_penalty}

    def set_params(self, **parameters):
        for parameter, value in parameters.items():
            setattr(self, parameter, value)
        return self

def main():
    #logger._init_logger()
    _logger = loggersp._logger
    comet = COMETSPLIT()

    param_grid = {'temperature': [0.0, 0.1,0.2,0.3,0.4],  
              'max_tokens': [1100], 
              'model':['gpt-4'],
              'top_p': [1],
              'frequency_penalty': [0.0, 0.1,0.2,0.3,0.4],
              'presence_penalty': [0]}  


    X_train = []
    Y_train = []


    for i in range(1,5):

        filename = "./test_set/split/split"+str(i)+".txt"
        file = open(filename, 'r')
        uc1 = file.read()
        file.close()

        X_train.append(uc1)

        filename = "./test_set/split/output"+str(i)+".txt"
        file = open(filename, 'r')
        uc1Sol = file.read()
        file.close()

        Y_train.append(uc1Sol)

    cv=4 #[(slice(None), slice(None))]
    grid = GridSearchCV(comet, param_grid, refit = False, verbose = 3,n_jobs=-1, cv=cv) #, scoring="accuracy") 

    # fitting the model for grid search 
    grid.fit(X_train, Y_train) 
 
    # print best parameter after tuning 
    _logger.debug("****** BEST CONFIG *****")
    _logger.debug(grid.best_params_) 
    _logger.debug(grid.best_score_)
    return 0

if __name__ == "__main__":
    main()

