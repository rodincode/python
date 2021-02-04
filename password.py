# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:13:27 2019

@author: LENOVO

password="Rohan"
enter=input("Enter Password::")
while enter!=password:
    enter=input("Please enter correct password::")
print("Access Granted")


print('Enter correct username and password combo to continue')
count=0
while count < 3:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if password=='Hytu76E' and username=='bank_admin':
        print('Access granted')
        break
    else:
        print('Access denied. Try again.')
        count += 1
        
name=" Rohan "
print(name)
"""
###########################################################################
#https://web.skype.com
website=input("Enter website address::")
print(website.split("."))
