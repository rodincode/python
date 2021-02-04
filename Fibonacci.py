# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 11:36:35 2019

@author: LENOVO
"""

#Make a program that prints the first ‘n’ fibonacci numbers, where n is defined by the user.
#x(n)= x(n-1) + x(n-2)
n=int(input("Type a value of n: "))
i=0
j=0
k=1
while i<=1:
    print(i)
    i+=1
while 1<i<=n:
    fibonacci= j+k
    j=k
    k=fibonacci
    print(fibonacci)
    i+=1
    
    
#Make a program that divides 2 numbers that are multiples  
#without using the division operator and prints the quotient. 
#Get the divisor and dividend from the user. 
divident=int(input("Enter the Divident: "))
divisor=int(input("Enter the Divisor: "))
#Divisor=Divident*Quotient + remainder
#since they are multiples of each other remainder=0
#quotient=divident/divisor
#[EXTRA] For number that are not multiples calculate and print the remainder
# and the quotient. Do not use any other operator except + and - operators.
quotient=0
while divident>=divisor:
    divident-=divisor
    quotient+=1
print("Quotient:",quotient)
print("Remainder:",divident)

#Print the following pattern: 
#12345
#23456
#34567
#45678
#56789
i=1
while i<=5:
    print(i,i+1,i+2,i+3,i+4)
    i+=1