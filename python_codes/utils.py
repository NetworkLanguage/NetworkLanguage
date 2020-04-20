#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import pandas as pd
import numpy as np
from sklearn.metrics import precision_recall_fscore_support, accuracy_score

def eval_model(y_true, y_pred):
    print("accuracy: ", accuracy_score(y_true, y_pred))
    # 计算每个分类的Precision, Recall, f1, support
    p, r, f1, s = precision_recall_fscore_support(y_true, y_pred)
    # 计算总体的平均Precision, Recall, f1, support
    tot_p = np.average(p, weights=s)
    tot_r = np.average(r, weights=s)
    tot_f1 = np.average(f1, weights=s)
    tot_s = np.sum(s)
    res1 = pd.DataFrame({
        u'Precision': p,
        u'Recall': r,
        u'F1': f1,
        u'Support': s
    })
    res2 = pd.DataFrame({
        u'Precision': [tot_p],
        u'Recall': [tot_r],
        u'F1': [tot_f1],
        u'Support':[tot_s]
    })
    res2.index = ['all']
    res = pd.concat([res2, res1])
    return res[[ 'Precision', 'Recall', 'F1', 'Support']]