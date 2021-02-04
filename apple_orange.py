# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 12:45:09 2019

@author: LENOVO
"""

from sklearn import tree
features = [[140,1], [130,1], [150,0], [170, 0]]
labels = [0,0,1,1]
target_names = ["Apple","orange"]
features_name = ["weight","texture"]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
#print(clf.predict([[160,0]])
# Generating visualization
from sklearn.externals.six import StringIO
import pydot
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data,feature_names=features_name,class_names=target_names,filled=True, rounded=True,impurity=False)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
#graph.write_pdf("fruit.pdf”)