# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 11:12:27 2019

@author: LENOVO
"""
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras import Sequential
import pandas as pd
#from keras.models import Sequential
from sklearn.model_selection import train_test_split
#from keras.layers import Dense
#import numpy as np

#load pima indians dataset

filename=r"C:\Users\lenovo\Downloads\Student_data - Sheet1.csv"
student_data=pd.read_csv(filename)
features=student_data.drop("passed",axis=1)
outcomes=student_data["passed"]
print(student_data.head())


features.shape
temp= len(student_data.loc[student_data.passed=="yes","passed"])
print(temp)



numerical_features=pd.get_dummies(features)
numerical_outcomes=outcomes.replace(["yes","no"],[1,0])
#splitting the data
x_train, x_test, y_train, y_test = train_test_split(numerical_features, numerical_outcomes,test_size=0.75,random_state=42)
#fix random seed for reproducibility
#numpy.random.seed(7)
#split into (X) and (Y) variables
#features=dataset[:,0:8]
#outcomes=dataset[:,8]

#create Model
model= Sequential()
model.add(Dense(22, input_dim=56, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

#Compile Model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

#fit the model
model.fit(numerical_features,numerical_outcomes,epochs=150, batch_size=10)

#evaluate the model
scores = model.evaluate(numerical_features,numerical_outcomes)
print('\n%s: %.2f%%' % (model.metrics_names[1], scores[1]*100))

#Ask Questions
age=int(input("What's the students age::"))
Medu=int(input("What's Medu::"))
Fedu=int(input("What's Fedu::"))
traveltime=int(input("What's traveltime::"))
studytime=int(input("What's studytime::"))
failures=int(input("How many failures::"))
famrel=int(input("What's famrel::"))
freetime=int(input("What's freetime::"))
goout=int(input("What's goout::"))
Dalc=int(input("What's Dalc::"))
Walc=int(input("What's Walc::"))
health=int(input("What's health::"))
absences=int(input("How many absences::"))
school_GP=int(input("Is the school_LPS::"))
school_MS=int(input("Is the school_VIVEK::"))
sex_F=int(input("Is the sex_F::"))
sex_M=int(input("Is the sex_M::"))
address_R=int(input("Is the address_r::"))
address_U=int(input("Is the address_U::"))
famsize_GT3=int(input("Is the famsize_GT3::"))
famsize_LE3=int(input("Is the famsize_LE3::"))
Pstatus_A=int(input("Is the Pstatus_A::"))
Pstatus_T=int(input("Is the Pstatus_T::"))
Mjob_at_home=int(input("Is Mjob_at_home::"))
Mjob_health=int(input("Is Mjob_health::"))
Mjob_other=int(input("Is Mjob_other::"))
Mjob_services=int(input("Is Mjob_service::"))
Mjob_teacher=int(input("Is Mjob_teacher::"))
Fjob_at_home=int(input("Is Fjob_at_home::"))
Fjob_health=int(input("Is Fjob_health::"))
Fjob_other=int(input("Is Fjob_other::"))
Fjob_services=int(input("Is Fjob_service::"))
Fjob_teacher=int(input("Is Fjob_teacher::"))
reason_course=int(input("Is the reason_course::"))
reason_home=int(input("Is the reason_home::"))
reason_other=int(input("Is the reason_other::"))
reason_reputation=int(input("Is the reason_reputation::"))
guardian_father=int(input("Is the guardian_father::"))
guardian_mother=int(input("Is the guardian_mother::"))
guardian_other=int(input("Is the guardian_other::"))
schoolsup_no=int(input("Is the schoolsup_no::"))
schoolsup_yes=int(input("Is the schoolsup_yes::"))
famsup_no=int(input("Is the famsup_no::"))
famsup_yes=int(input("Is the famsup_yes::"))
paid_no=int(input("Is paid_no::"))
paid_yes=int(input("Is paid_yes::"))
activities_no=int(input("Is the activities_no::"))
activities_yes=int(input("Is the activities_yes::"))
nursery_no=int(input("Is the nursery_no::"))
nursery_yes=int(input("Is the nursury_yes::"))
higher_no=int(input("Is the higher_no::"))
higher_yes=int(input("Is the higher_yes::"))
internet_no=int(input("Is internet_no::"))
internet_yes=int(input("Is internet_yes::"))
romantic_no=int(input("Is romantic_no::"))
romantic_yes=int(input("Is romantic_yes::"))

#calculate pridictions
sample=[[age, Medu, Fedu, traveltime, studytime, failures, famrel, freetime, 
        goout, Dalc, Walc, health, absences, school_GP, school_MS, sex_F, 
        sex_M, address_R, address_U, famsize_GT3, famsize_LE3, Pstatus_A, Pstatus_T,
        Mjob_at_home, Mjob_health, Mjob_other, Mjob_services, Mjob_teacher,
        Fjob_at_home, Fjob_health, Fjob_other, Fjob_services, Fjob_teacher, 
        reason_course, reason_home, reason_other, reason_reputation,
        guardian_father, guardian_mother, guardian_other, schoolsup_no,
        schoolsup_yes, famsup_no, famsup_yes, paid_no, paid_yes, activities_no,
        activities_yes, nursery_no, nursery_yes, higher_no, higher_yes,
        internet_no, internet_yes, romantic_no, romantic_yes]]
predict=model.predict(sample)
print(" ")
if predict<0.5:
    print("The student may suffer in the examination")
else:
    print("The student is likely to pass the examination")
