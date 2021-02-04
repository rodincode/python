# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 12:33:35 2020

@author: LENOVO
"""

import pandas as pd
import numpy as np
filename=r"C:\Users\LENOVO\Downloads\titanic_data.csv"
df= pd.read_csv(filename)
df.head(5)
df.tail(5)

most_expensive=df[['company','price']][df.price==df['price'].max()]
print(most_expensive)

car_manufacturers=df.groupby('company')
toyota=car_manufacturers.get_group('toyota')
print('toyota')

df['company'].value_counts()

car_manufactures=df.groupby('company')
highest_price= car_manufacturers['company','price'].max()
print(highest_price)

car_manufactures=df.groupby('company')
mileage= car_manufacturers['company','average_mileage'].mean()
print(mileage)