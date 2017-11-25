# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 19:21:26 2017

@author: huhu
"""
import pandas as pd
from pandas import DataFrame,merge



labelAdd = pd.read_csv("f:/p2p/code/data/labelAdd.csv",error_bad_lines=False)    #读取全部信息

#%%  去掉failNum中汉字

"""
f=labelAdd['failNum']
flit=[]
for i in f:
    flit.append(str(i).split()[0])
failNum=DataFrame(flit)         #将list转为DataFrame
labelAdd['failNum']=failNum 
print labelAdd['failNum']
#%%  去掉successNum中汉字
lit=[]
s=labelAdd['successNum']
#print s.str.len()
for i in s:
    lit.append(str(i).split()[0])
#print lit
successNum=DataFrame(lit)         #将list转为DataFrame
labelAdd['successNum']=successNum                      #将数值化之后的性别值输入到user数据框中

#%%去掉month中汉字
mlit=[]
m=labelAdd['months']
for i in m:
    mlit.append(str(i).split()[0])
months=DataFrame(mlit)         #将list转为DataFrame
labelAdd['months']=months 
print labelAdd['months']
"""
#%%  对borrowCredit去掉汉字
borrowlit=[]
borrow=labelAdd['borrowCredit']
for i in borrow:
    borrowlit.append(str(i).split()[0])
borrowLeft=DataFrame(borrowlit)         #将list转为DataFrame
labelAdd['borrowCredit']=borrowLeft 
print labelAdd['borrowCredit']
#%% 对investCredit去掉汉字
investlit=[]
invest=labelAdd['investCredit']
for i in invest:
    investlit.append(str(i).split()[0])
investCredit=DataFrame(investlit)         #将list转为DataFrame
labelAdd['investCredit']=investCredit 
print labelAdd['investCredit']




#%%
"""
#%%   下面代码段对标签信息进行映射  已还完为1 其余映射0 存到y.csv
label=pd.read_csv("f:/p2p/code/data/b.csv",error_bad_lines=False)  #读取标签信息
state =label['state']    #查看sex中不同的值
list = []                #list用来存数值化后的结果
for s in state.values:
    if s=='\xe5\xb7\xb2\xe8\xbf\x98\xe5\xae\x8c':   #男对应1
        list.append(1)
    else:  
        list.append(0)      #未知对应3    可以去掉      

df=DataFrame(list)         #将list转为DataFrame
label['state']=df                      #将数值化之后的性别值输入到user数据框中
label.to_csv("f:/p2p/code/data/y.csv",index=False)
#%%
"""