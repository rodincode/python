# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 18:43:33 2020

@author: dell
"""

#STEP 1: Import Libraries
import sklearn
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

#STEP 2: Load Data
data = load_breast_cancer()
label_names = data['target_names']
labels = data['target']
feature_names = data['feature_names']
features = data['data']
print(label_names)
print(labels[0])
print(feature_names[0])
print(features[0])

#STEP 3: Organize the Data
train, test, train_labels, test_labels = train_test_split(features,labels,test_size = 0.40, random_state = 42)

#STEP 4: Train the classifier
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
model = gnb.fit(train, train_labels)

#STEP 5: Evaluate and predict
prediction = gnb.predict(test)
print("PREDICTION:: ",prediction)
#Accuracy
from sklearn.metrics import accuracy_score
print("ACCURACY:: ",accuracy_score(test_labels,prediction))

print("")
print("")

#Using Logistic Regression Algorithm to the Training Set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(train, train_labels)
prediction1 = classifier.predict(test)
print("Logistic Regression: ",prediction1)
print("Logistic Regression Score: ",accuracy_score(test_labels,prediction1))
print("")
print("")

#Using KNeighborsClassifier Method of neighbors class to use Nearest Neighbor algorithm
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
classifier.fit(train, train_labels)
prediction2 = classifier.predict(test)
print("KNeighbors: ",prediction2)
print("Kneighbors Score: ",accuracy_score(test_labels,prediction2))
print("")
print("")

#Using SVC method of svm class to use Support Vector Machine Algorithm
from sklearn.svm import SVC
classifier = SVC(kernel = 'linear', random_state = 0)
classifier.fit(train, train_labels)
prediction3 = classifier.predict(test)
print("SVM: ",prediction3)
print("SVM Score: ",accuracy_score(test_labels,prediction3))
print("")
print("")

#Using SVC method of svm class to use Kernel SVM Algorithm
from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 0)
classifier.fit(train, train_labels)
prediction4 = classifier.predict(test)
print("Kernel SVM: ",prediction4)
print("Kernel SVM Score: ",accuracy_score(test_labels,prediction4))
print("")
print("")

#Using GaussianNB method of naïve_bayes class to use Naïve Bayes Algorithm
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(train, train_labels)
prediction5 = classifier.predict(test)
print("GaussianNB: ",prediction5)
print("GaussianNB Score: ",accuracy_score(test_labels,prediction5))
print("")
print("")

#Using DecisionTreeClassifier of tree class to use Decision Tree Algorithm
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
classifier.fit(train, train_labels)
prediction6 = classifier.predict(test)
print("Decision Tree: ",prediction6)
print("Decision Tree Score: ",accuracy_score(test_labels,prediction6))
print("")
print("")

#Using RandomForestClassifier method of ensemble class to use Random Forest Classification algorithm
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
classifier.fit(train, train_labels)
prediction7 = classifier.predict(test)
print("Random Forest: ",prediction7)
print("Random Forest Score: ",accuracy_score(test_labels,prediction7))
print("")
print("")


import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix
pred=[prediction, prediction1,prediction2, prediction3, prediction4,prediction5, prediction6, prediction7]
cm= np.array(confusion_matrix(test_labels,prediction4, labels=[1,0]))
confusion=pd.DataFrame(cm,index=['is_cancer', 'is_healthy'],columns=['predicted_cancer','predicted_healthy'])
sns.heatmap(confusion,annot=True)






