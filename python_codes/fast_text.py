#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from types import MethodType, FunctionType
import jieba
import fasttext.FastText as fasttext
import numpy as np
import os
from utils import eval_model

# 数据预处理
def clean_txt(raw):
    fil = re.compile(r"[^0-9a-zA-Z\u4e00-\u9fa5]+")
    return fil.sub(' ', raw)

def seg(sentence, sw, apply=None):
    if isinstance(apply, FunctionType) or isinstance(apply, MethodType):
        sentence = apply(sentence)
    return ' '.join([i for i in jieba.cut(sentence) if i.strip() and i not in sw])

def stop_words():
    with open('data/stopwords.txt', 'r', encoding='utf-8') as swf:
        return [line.strip() for line in swf]

def generate_train_test_data(train_file_o, test_file_o, train_file, test_file):

    train_texts = open(train_file_o, "r", encoding="utf-8")
    train_texts = train_texts.readlines()

    test_texts = open(test_file_o, "r", encoding="utf-8")
    test_texts = test_texts.readlines()

    with open(train_file, 'w', encoding='utf-8') as trainf, \
            open(test_file, 'w', encoding='utf-8') as testf:
        for index, text in enumerate(train_texts):
            y = text.split('\t')[0]
            label = "__label__" + y
            words = seg(text.split("\t")[1].lower().replace('\n', ''), stop_words(), apply=clean_txt)
            trainf.write(label+" , "+words+"\n")
        for index, text in enumerate(test_texts):
            y = text.split('\t')[0]
            label = "__label__" + y
            words = seg(text.split("\t")[1].lower().replace('\n', ''), stop_words(), apply=clean_txt)
            testf.write(label+" , "+words+"\n")

def train_model(ipt=None, opt=None, model='', dim=128, epoch=5, lr=0.1, loss='softmax'):
    np.set_printoptions(suppress=True)
    if os.path.isfile(model):
        classifier = fasttext.load_model(model)
    else:
        classifier = fasttext.train_supervised(ipt, label='__label__', dim=dim, epoch=epoch,
                                               lr=lr, wordNgrams=2, loss=loss)
        classifier.save_model(opt)
    return classifier

def evaluate(file, classifier):
    y_test, y_pred = [], []
    with open(file, encoding="utf-8") as f:
        for line in f:
            label, content = line.split(',', 1)
            y_test.append(label.strip().strip('__label__'))
            labels2 = classifier.predict([seg(sentence=content.strip(), sw='', apply=clean_txt)])
            pre_label, sim = labels2[0][0][0], labels2[1][0][0]
            y_pred.append(pre_label.strip().strip('__label__'))
    print(eval_model(y_test, y_pred))

if __name__ == '__main__':
    # task = "weibo_gender"
    # task = "weibo_area"
    task = "douban"

    dim = 128
    lr = 5
    epoch = 100

    train_file_o = f'data/{task}_train.txt'
    test_file_o = f'data/{task}_test.txt'
    train_file = f'models/fasttext_{task}_train_seg.txt'
    test_file = f'models/fasttext_{task}_test_seg.txt'

    if not os.path.isfile(train_file):
        generate_train_test_data(train_file_o, test_file_o, train_file, test_file)
    if not os.path.isfile(test_file):
        generate_train_test_data(test_file_o, test_file_o, train_file, test_file)

    model = f'models/fasttext_{task}_data_dim{str(dim)}_lr0{str(lr)}_iter{str(epoch)}.model'

    classifier = train_model(ipt=train_file,
                             opt=model,
                             model=model,
                             dim=dim, epoch=epoch, lr=0.5
                             )

    result = classifier.test(test_file)
    print(result)

    evaluate(test_file, classifier)