#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pandas as pd
import numpy as np
import jieba
import sklearn.naive_bayes as nb
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from utils import eval_model


def data_processing(train_df, test_df):
	con_list_train = []
	con_list_test = []
	for c in train_df.content.values:
    	con_list_train.append(' '.join(jieba.lcut(c, cut_all=False)))
    for c in test_df.content.values:
    	ccon_list_test.append(' '.join(jieba.lcut(c, cut_all=False)))
    new_train_df = pd.DataFrame({
    	'class': train_df['class'],
    	'content': con_list_train
    	})
    new_test_df = pd.DataFrame({
    	'class': test_df['class'],
    	'content': con_list_test
    	})

    return new_train_df['content'].values, new_train_df['class'].values, new_test_df['content'].values, new_test_df['class'].values


def predict_model(train_df, test_df):
	train_data, train_y, test_data, test_y = data_processing(train_df, test_df)
	cv = CountVectorizer()
	train_tfmat = cv.fit_transform(train_data)

	tf = TfidfTransformer()
	train_x = tf.fit_transform(train_tfmat)

	test_tfmat = cv.transform(test_data)
	test_x = tf.transform(test_tfmat)

	model_nb = nb.MultinomialNB()
	model_lr = LogisticRegression()
	model_nn = MLPClassifier(hidden_layer_sizes=(100,100), early_stopping=True)

	model_names = ['NN', 'NB', 'LR']
	models = [model_nn, model_nb, model_lr]

	for _, clf in enumerate(models):
		print("Model {}: {}".format(_+1, model_names[_]))
        clf.fit(train_x, train_y)
        y_pred = clf.predict(test_x)
        result = eval_model(test_y, y_pred)
        print(result)


if __name__ == '__main__':
	# task = "weibo_gender"
	# task = "weibo_area"
	task = "douban"

	train_file_o = f'data/{task}_train.txt'
	test_file_o = f'data/{task}_test.txt'

	train_df = pd.read_csv(train_file_o, header=None, sep='\t')
	test_df = pd.read_csv(test_file_o, header=None, sep='\t')

	train_df.columns = ['class', 'content']
	test_df.columns = ['class', 'content']

	predict_model(train_df, test_df)
