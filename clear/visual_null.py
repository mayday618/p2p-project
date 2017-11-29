# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 19:21:26 2017

@author: huhu
"""
import pandas as pd
from pandas import DataFrame,merge
data = pd.read_csv("f:/p2p/code/category_data.csv",error_bad_lines=False)#读取x
print data.count()
del data['bidNumbers']
del data['bidScore']
del data['receiveFullScore']
del data['receiveScore']
del data['overScore']
print data.count()
data.fillna(data.mean())