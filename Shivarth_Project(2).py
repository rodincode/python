# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 13:26:46 2019

@author: LENOVO
"""

import pandas as pd 


filename = r"C:\Users\LENOVO\Downloads\Tweets.csv"


df = pd.read_csv(filename,encoding="unicode_escape")


all_data = df.drop_duplicates(keep='first', inplace=False)
cleaned_data = all_data.dropna()


sentences = cleaned_data['text']


y = cleaned_data['airline_sentiment']

numerical_outcomes=y.replace(["positive","negative","neutral"],[1,0,2])

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
eng_stops = set(stopwords.words('english'))

# Create word tokens

def removing_stop_words(sentences):
    no_stops=[]
    for word in sentences:
        if word not in eng_stops:
            new_sentences=no_stops.append(word)

new_sentences=removing_stop_words(sentences)

from sklearn.model_selection import train_test_split # imports module from package

x_train, x_test, y_train, y_test = train_test_split(new_sentences, y, test_size=0.25, random_state=1000)

from sklearn.feature_extraction.text import CountVectorizer
#from io import StringIO

vectorizer = CountVectorizer()

vectorizer.fit(x_train)

#docs_new_train = [ StringIO.StringIO(x) for x in x_train]
#docs_new_test = [ StringIO.StringIO(x) for x in x_test]

X_train = vectorizer.transform(x_train)

X_test  = vectorizer.transform(x_test)



from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression()

classifier.fit(X_train, y_train)

score = classifier.score(X_test, y_test)

print("\n Accuracy:", score)   #model accuracy

#

#########################################################

###Predicting the sentiment of user input

#########################################################

txt = input("Enter expression: ")

test_sentences = [txt]

test_bag = vectorizer.transform(test_sentences)

result_label = classifier.predict(test_bag)         #predicting the class

result_score = classifier.predict_proba(test_bag)   #Probobilities of belonging to both classes

#

if result_label==1:

    print("Positive", result_score)

else:   

    print("Negative", result_score)
    