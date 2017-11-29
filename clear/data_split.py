# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 19:21:26 2017

@author: huhu
"""
import pandas as pd
from pandas import DataFrame,merge
from sklearn.cross_validation import train_test_split


x = pd.read_csv("f:/p2p/code/category_data.csv",error_bad_lines=False)#读取x
y = pd.read_csv("f:/p2p/code/data/y.csv",error_bad_lines=False)#读取y
x_y = merge(x,y,on="bidId",how='left')
X=x_y.iloc[:,:-1]
y=x_y.iloc[:,-1:]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
X_train.to_csv("f:/p2p/code/data/X_train.csv",index=False)
y_train.to_csv("f:/p2p/code/data/y_train.csv",index=False)
X_test.to_csv("f:/p2p/code/data/X_test.csv",index=False)
y_test.to_csv("f:/p2p/code/data/y_test.csv",index=False)
