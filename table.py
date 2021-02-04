# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 15:37:52 2019

@author: LENOVO

a=1
while a<10:
    for i in range(0,10,1):
        print(a,"x",i,"=",a*i)
    a+=1
    
    
i=1
while i<10:
    print(i)
    i=i+1
    
    

user=input("Please type the password: ")
while user!="priyanka":
    user=input("Please type the password: ")
print("Access Granted!")


user2=int(input("Enter the number: "))
if user2>10:
    print("The number is greater than 10")
elif user2<10:
    print("The number is less than 10")
else:
    print("The number is 10")
    
    
side1=int(input("Enter the first side: "))
side2=int(input("Enter the second side: "))
side3=int(input("Enter the third side: "))
if (side1+side2>side3) and (side2+side3>side1) and (side1+side3>side2):
    print("Its a valid triangle")
else:
    print("Its not a valid traingle")
    
"""
    
    
    
num=int(input("Enter a number: "))
if num>10:
    if num<5:
        print("The number is less than 5")
    else:
        print("The number is greater than 5 but less than 10")
else:
    print("The number is greater than 10")
    