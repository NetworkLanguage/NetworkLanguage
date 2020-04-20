#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jieba
import re
import time
import numpy as np
import multiprocessing
import gensim
import os
from gensim.models import Word2Vec
# 警告信息
import warnings
warnings.filterwarnings('ignore')
print('gensim version = ',gensim.__version__)

def preprecess(train_file_o, test_file_o):
    sentences_train = []
    sentences_test = []
    labels_train = []
    labels_test = []

    stopword_list = [k.strip() for k in open('data/stopwords.txt', encoding='utf-8') if k.strip() != '']
    def segment(sentence):
        sentence = sentence.replace('\n', '')
        sentence = re.sub('[0-9a-zA-Z]','',sentence)
        words_list = [k for k in jieba.cut(sentence) if k not in stopword_list]
        return words_list

    with open(train_file_o, 'r', encoding='utf8') as f:
        lines = f.readlines()
        for line in lines:
            splits = line.split('\t')
            feat = segment(splits[1])
            label = int(splits[0])
            sentences_train.append(feat)
            labels_train.append(label)

    with open(test_file_o, 'r', encoding='utf8') as f:
        lines = f.readlines()
        for line in lines:
            splits = line.split('\t')
            feat = segment(splits[1])
            label = int(splits[0])
            sentences_test.append(feat)
            labels_test.append(label)

    return sentences_train, sentences_test, labels_train, labels_test

def train_word2vec(sentences_train, sentences_test, dim, iter):
    '''
    :param dim: 词向量维度
    :param iter: 训练轮次
    :return: word2vec model
    '''
    model = Word2Vec(sentences_train+sentences_test, size=dim, window=5, min_count=5,
                     iter=iter, workers=multiprocessing.cpu_count())
    return model

def get_words_vec(words, model):
    '''
    获取句子的向量：所有单词向量平均
    :param model: word2vec模型
    '''
    w2v_sum = []
    total = 0
    for word in words:
        try:
            w2v_tmp = model[word]
            total = total + 1
            if len(w2v_sum) > 0:
                w2v_sum = list(np.array(w2v_tmp) + np.array(w2v_sum))
            else:
                w2v_sum = list(np.array(w2v_tmp))
        except Exception as e:
            pass

    if len(w2v_sum) == dim:
        w2v_documents = [float("{:.6f}".format(w2v / total)) for w2v in w2v_sum]
        return w2v_documents
    else:
        return []

def generate_train_test_data(train_file_o, test_file_o, train_file_w2v, test_file_w2v, dim, iter):
    '''
    :param dim: word2vec词向量维度
    :param iter: word2vec训练轮次
    :return: word2vec特征
    '''
    sentences_train, sentences_test, labels_train, labels_test = preprecess(train_file_o, test_file_o)
    model = train_word2vec(sentences_train, sentences_test, dim, iter)

    X_train, X_test = [], []  # doc2vec 特征
    y_train, y_test = [], []  # 文本行的label
    for index, sentence in enumerate(sentences_train):
        words_list = sentence
        words_list_doc2vec = get_words_vec(words_list, model)
        if len(words_list_doc2vec) > 0:
            X_train.append(words_list_doc2vec)
        else:
            X_train.append([0 for i in range(dim)])
        y_train.append(labels_train[index])

    for index, sentence in enumerate(sentences_test):
        words_list = sentence
        words_list_doc2vec = get_words_vec(words_list, model)
        if len(words_list_doc2vec) > 0:
            X_test.append(words_list_doc2vec)
        else:
            X_test.append([0 for i in range(dim)])
        y_test.append(labels_test[index])

    # word2vec 特征保存
    with open(train_file_w2v, 'w') as f:
        for i in range(len(X_train)):
            x_str = [str(x) for x in list(X_train[i])]
            results = "{} {}".format(y_train[i]," ".join(x_str))
            f.write('{}\n'.format(results))

    with open(test_file_w2v, 'w') as f:
        for i in range(len(X_test)):
            x_str = [str(x) for x in list(X_test[i])]
            results = "{} {}".format(y_test[i]," ".join(x_str))
            f.write('{}\n'.format(results))

def predict_model(trainfile, testfile):

    X_train, X_test = [], []  # doc2vec 特征
    y_train, y_test = [], []  # 文本行的label
    with open(trainfile,'r') as fr:
        lines = fr.readlines()
        for line in lines:
            line = line.strip()
            feat = [float(f) for f in line.split()[1:]]
            X_train.append(feat) # 特征列
            y_train.append(int(line.split()[0]))#Label 列

    with open(testfile.format(iter),'r') as fr:
        lines = fr.readlines()
        for line in lines:
            line = line.strip()
            feat = [float(f) for f in line.split()[1:]]
            X_test.append(feat) # 特征列
            y_test.append(int(line.split()[0]))#Label 列

    from sklearn.linear_model import LogisticRegression
    from sklearn.neural_network import MLPClassifier
    import sklearn.naive_bayes as nb
    from utils import eval_model

    lr = LogisticRegression()
    model_nb = nb.GaussianNB()
    nn = MLPClassifier(hidden_layer_sizes=(100,100), early_stopping=True)

    model_names = [ "NN", "NB", "LR"]
    models = [nn, model_nb, lr]

    X_train = np.array(X_train)
    X_test = np.array(X_test)
    y_train = np.array(y_train)
    y_test = np.array(y_test)
    # print(y_train, y_test)
    for _, clf in enumerate(models):
        print("Model {}: {}".format(_+1, model_names[_]))
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        result = eval_model(y_test, y_pred)
        print(result)

if __name__ == '__main__':
    # task = "weibo_gender"
    # task = "weibo_area"
    task = "douban"

    dim = 128  # word2vec的词向量维度
    iter = 100

    train_file_o = f'data/{task}_train.txt'
    test_file_o = f'data/{task}_test.txt'
    train_file_w2v = f'models/w2v_{task}_train_iter{str(iter)}.txt'
    test_file_w2v = f'models/w2v_{task}_test_iter{str(iter)}.txt'

    if not os.path.isfile(train_file_w2v):
        generate_train_test_data(train_file_o, test_file_o, train_file_w2v, test_file_w2v, dim, iter)

    if not os.path.isfile(test_file_w2v):
        generate_train_test_data(test_file_o, test_file_o, train_file_w2v, test_file_w2v, dim, iter)

    predict_model(train_file_w2v, test_file_w2v)