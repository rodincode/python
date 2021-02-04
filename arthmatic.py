# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 17:17:54 2019

@author: LENOVO
"""

a=int(input("a="))
b=int(input("b="))
add=a+b
sub=a-b
mul=a*b
div=a/b
mod=a%b
floor_div=a//b
print("addittion=",add)
print("substraction=",sub)
print("multiply",mul)
print("division",div)
print("modulus=", mod)
print("floor division=",floor_div)
import math
square_root=math.sqrt(mul)
import numpy as np


for i in range(1,11,1):
    for j in range(1,11,1):
        print(i,"x",j,"=",i*j)
        print("")
        
fac= int(input("Which factorial: "))
for i in range(1,fac,1):
    fac=fac*i
print(fac)
    