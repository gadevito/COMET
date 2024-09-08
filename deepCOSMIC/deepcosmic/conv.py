from gensim.scripts.glove2word2vec import glove2word2vec

glove_input_file = 'w2v_glove.6B.300d.txt'
word2vec_output_file = 'w2v_glove.6B.300d.word2vec.txt'
glove2word2vec(glove_input_file, word2vec_output_file)