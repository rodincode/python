# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 15:02:38 2019

@author: ACER
"""

from sklearn.tree import DecisionTreeClassifier
#features = [[140,'smooth'], [130,'smooth'], [150,'bumpy'], [170, 'bumpy']]
#labels = ['apple','apple','orange','orange']

#smooth =1;bumpy=0; apple =0; orange=1
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = [0, 0, 1, 1]
 
clf = DecisionTreeClassifier() 
clf.fit(features, labels)
 

print(clf.predict([[160, 0]]))

#y_pred = clf.predict(features)
print(clf.score(features,labels))
# Output: 0-apple, 1-orange
# Correct output is: 1-orange


