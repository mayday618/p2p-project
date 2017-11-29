# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 18:06:12 2017

@author: huhu
"""
import pandas as pd
from pandas import DataFrame,merge
import numpy as np

data = pd.read_csv("f:/p2p/p2p-project/data/map_data/clear_data.csv",error_bad_lines=False)    #读取全部信息

"""
print data['class'].value_counts()
print data['averageCapital'].value_counts()
print data['sex'].value_counts()
print data['age'].value_counts()
print data['identity'].value_counts()
print data['otherCertification'].value_counts()
"""

#这里统一用0来代表不是缺失值中的未知值或者数量相对太少的类别

#%%  对class进行映射
print data['class'].value_counts()
data['class'].loc[(data['class'] == 'A')] = 1
data['class'].loc[(data['class'] == 'B')] = 2
data['class'].loc[(data['class'] == 'C')] = 3
data['class'].loc[(data['class'] == 'D')] = 4
data['class'].loc[(data['class'] == 'E')] = 5
data['class'].loc[(data['class'] == 'F')] = 6
data['class'].loc[(data['class'] == 'AA')] = 7
data['class'].loc[(data['class'] == 'AAA')] = 8
data['class'].loc[(data['class'] == 'http://www.ppdai.com/user/thomasy')] = 0
print data['class'].value_counts()
#%% 对sex进行映射
print data['sex'].value_counts()
data['sex'].loc[(data['sex'] == '男')] = 1
data['sex'].loc[(data['sex'] == '女')] = 2
data['sex'].loc[(data['sex'] == '未知')] = 0
print data['sex'].value_counts()

#%% 对age进行映射
print data['age'].value_counts()
data['age'].loc[(data['age'] == '26-31岁')] = 1
data['age'].loc[(data['age'] == '20-25岁')] = 2
data['age'].loc[(data['age'] == '32-38岁')] = 3
data['age'].loc[(data['age'] == '大于39岁')] = 4
data['age'].loc[(data['age'] == '未知')] = 0
print data['age'].value_counts()
#%% 对identity进行映射
print data['identity'].value_counts()
data['identity'].loc[(data['identity'] == '目前身份：工薪族')] = 1
data['identity'].loc[(data['identity'] == '目前身份：私营业主')] = 2
data['identity'].loc[(data['identity'] == '目前身份：网店卖家')] = 3
data['identity'].loc[(data['identity'] == '目前身份：学生')] = 4
data['identity'].loc[(data['identity'] == '目前身份：其他')] = 0
data['identity'].loc[(data['identity'] == '目前身份：0')] = 0
data['identity'].loc[(data['identity'] == '目前身份：')] = 0
data['identity'].loc[(data['identity'] == '目前身份：5')] = 0
print data['identity'].value_counts()
#%% 对averageCapital进行映射
print data['averageCapital'].value_counts()
data['averageCapital'].loc[(data['averageCapital'] == '等额本息')] = 1
data['averageCapital'].loc[(data['averageCapital'] == '月还息，季还1/4本金')] = 0
data['averageCapital'].loc[(data['averageCapital'] == '一次还本付息')] = 0
print data['averageCapital'].value_counts()
#%% 对otherCertification进行映射
print data['otherCertification'].value_counts()
data['otherCertification'].loc[(data['otherCertification'] == '其他认证：3 分网上银行充值认证(3分)')] = 1
data['otherCertification'].loc[(data['otherCertification'] == '其他认证：0 分网上银行充值认证(3分)')] = 2
print data['otherCertification'].value_counts()
del data['name']
del data['state']
data.to_csv("f:/p2p/code/category_data.csv",index=False)