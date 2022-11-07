# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 10:29:08 2022

@author: CHuang
"""

import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt

#%%

def cal_auc(label,pred,pos_label=1):
    fpr, tpr, thresholds = metrics.roc_curve(label, pred, pos_label=pos_label)
    auc = metrics.auc(fpr, tpr)
    
    return auc,(fpr, tpr, thresholds)


def plot_simiple_roc(fpr,tpr,auc):
    #create ROC curve
    plt.plot(fpr,tpr)
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    plt.plot(fpr,tpr,label="AUC="+str(auc))
    plt.legend(loc=4)
    plt.show()
    


#%%
if __name__ =="__main__":
    y = np.array([1, 1, 2, 2])
    pred = np.array([0.1, 0.4, 0.35, 0.8])
    auc,(fpr, tpr, thresholds) = cal_auc(y, pred, pos_label=2)
    plot_simiple_roc(fpr,tpr,auc)
    