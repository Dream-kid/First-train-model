# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 13:22:28 2019

@author: lenovo
"""

from sklearn.linear_model import LinearRegression
from random import randint
train_limit= 1000
train_count = 100

train_input=list()
train_output=list()

for i in range (train_count):
    a=randint(0,train_limit)
    b=randint(0,train_limit)
    c=randint(0,train_limit)
    opp= a + 2*b + 3*c
    train_input.append([a,b,c])
    train_output.append(opp)


predictor = LinearRegression(n_jobs=-1)
predictor.fit(X=train_input, 
              y=train_output)


X_TEST = [[10, 20, 30]]
outcome = predictor.predict(X=X_TEST)
coefficients = predictor.coef_

print('Outcome : {}\nCoefficients : {}'.format(outcome, coefficients))    