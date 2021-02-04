# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 16:09:50 2019

@author: LENOVO
"""
##Machine Learning#################### 
from sklearn import tree
# dataset
features = [[150,1],[170,1],[140,0],[130,0]]
outcomes = [0, 0,1,1]
#4 steps---(1)Load the datset, 
#(2)Introduce the classifier, 
#(3)classifier.fit, 
#(4) classifier.predict
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,outcomes)
result = clf.predict([[160,1]])

print(result)


