# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 19:21:26 2017

@author: huhu
"""
import pandas as pd
from pandas import DataFrame,merge



labelAdd = pd.read_csv("f:/p2p/code/data/labelAdd.csv",error_bad_lines=False)    #读取全部信息

#%%  去掉failNum中汉字
f=labelAdd['failNum']
flit=[]
for i in f:
    if i!='nan':
        flit.append(str(i).split()[0])
failNum=DataFrame(flit)         #将list转为DataFrame
labelAdd['failNum']=failNum 
#%%  去掉successNum中汉字
lit=[]
s=labelAdd['successNum']
#print s.str.len()
for i in s:
    if i!='nan':
        lit.append(str(i).split()[0])
#print lit
successNum=DataFrame(lit)         #将list转为DataFrame
labelAdd['successNum']=successNum                      #将数值化之后的性别值输入到user数据框中
#%%去掉month中汉字
mlit=[]
m=labelAdd['months']
for i in m:
    if i!='nan':
        mlit.append(str(i).split()[0])
months=DataFrame(mlit)         #将list转为DataFrame
labelAdd['months']=months 
#%%  对borrowCredit去掉汉字
borrowlit=[]
borrow=labelAdd['borrowCredit']
for i in borrow:
    if i!='nan':
        borrowlit.append(str(i).split()[0])
borrowLeft=DataFrame(borrowlit)         #将list转为DataFrame
labelAdd['borrowCredit']=borrowLeft 
#%%  对bidNumbers去掉汉字
bidNumberslit=[]
bidNumbers=labelAdd['bidNumbers']
for i in bidNumbers:
    if i!='nan':
        bidNumberslit.append(str(i).split()[0])
bidNumbers=DataFrame(bidNumberslit)         #将list转为DataFrame
labelAdd['bidNumbers']=bidNumbers 
#%%  对Authentication去掉汉字
Authenticationlit=[]
Authentication=labelAdd['Authentication']
for i in Authentication:
    if i!='nan':
        Authenticationlit.append(str(i).split()[0])
Authentication=DataFrame(Authenticationlit)         #将list转为DataFrame
labelAdd['Authentication']=Authentication 
#%%  对videoCertification去掉汉字
videoCertificationlit=[]
videoCertification=labelAdd['videoCertification']
for i in videoCertification:
    if i!='nan':
        videoCertificationlit.append(str(i).split()[0])
videoCertification=DataFrame(videoCertificationlit)         #将list转为DataFrame
labelAdd['videoCertification']=videoCertification 
#%%  对educationCertification去掉汉字
educationCertificationlit=[]
educationCertification=labelAdd['educationCertification']
for i in educationCertification:
    if i!='nan':
        educationCertificationlit.append(str(i).split()[0])
educationCertification=DataFrame(educationCertificationlit)         #将list转为DataFrame
labelAdd['educationCertification']=educationCertification 
#%%  对phoneCertification去掉汉字
phoneCertificationlit=[]
phoneCertification=labelAdd['phoneCertification']
for i in phoneCertification:
    if i!='nan':
        phoneCertificationlit.append(str(i).split()[0])
phoneCertification=DataFrame(phoneCertificationlit)         #将list转为DataFrame
labelAdd['phoneCertification']=phoneCertification 
#%%  对fullClearScore去掉汉字
fullClearScorelit=[]
fullClearScore=labelAdd['fullClearScore']
for i in fullClearScore:
    if i!='nan':
        fullClearScorelit.append(str(i).split()[0])
fullClearScore=DataFrame(fullClearScorelit)         #将list转为DataFrame
labelAdd['fullClearScore']=fullClearScore 
#%%  对overPayScore去掉汉字
overPayScorelit=[]
overPayScore=labelAdd['overPayScore']
for i in overPayScore:
    if i!='nan':
        overPayScorelit.append(str(i).split()[0])
overPayScore=DataFrame(overPayScorelit)         #将list转为DataFrame
labelAdd['overPayScore']=overPayScore 
#%%  对bidScore去掉汉字
bidScorelit=[]
bidScore=labelAdd['bidScore']
for i in bidScore:
    if i!='nan':
        bidScorelit.append(str(i).split()[0])
bidScore=DataFrame(bidScorelit)         #将list转为DataFrame
labelAdd['bidScore']=bidScore 
#%%  对receiveFullScore去掉汉字
receiveFullScorelit=[]
receiveFullScore=labelAdd['receiveFullScore']
for i in receiveFullScore:
    if i!='nan':
        receiveFullScorelit.append(str(i).split()[0])
receiveFullScore=DataFrame(receiveFullScorelit)         #将list转为DataFrame
labelAdd['receiveFullScore']=receiveFullScore 
#%% 对overScore去掉汉字
overScorelit=[]
overScore=labelAdd['overScore']
for i in overScore:
    if i!='nan':
        overScorelit.append(str(i).split()[0])
overScore=DataFrame(overScorelit)         #将list转为DataFrame
labelAdd['overScore']=overScore 
#%%  对receiveScore去掉汉字
receiveScorelit=[]
receiveScore=labelAdd['receiveScore']
for i in receiveScore:
    if i!='nan':
        receiveScorelit.append(str(i).split()[0])
receiveScore=DataFrame(receiveScorelit)         #将list转为DataFrame
labelAdd['receiveScore']=receiveScore 
#%% 对investCredit去掉汉字
investlit=[]
invest=labelAdd['investCredit']
for i in invest:
    if i!='nan':
        investlit.append(str(i).split()[0])
investCredit=DataFrame(investlit)         #将list转为DataFrame
labelAdd['investCredit']=investCredit 
#%%  去掉money的￥ 

moneylit=[]
money=labelAdd['money']
for i in money:
    if i!='nan':
        moneylit.append(str(i)[2:])
money=DataFrame(moneylit)         #将list转为DataFrame
labelAdd['money']=money

#%%  去掉rate的% 

ratelit=[]
rate=labelAdd['rate']
for i in rate:
    if i!='nan':
        ratelit.append(str(i)[:-1])
rate=DataFrame(ratelit)         #将list转为DataFrame
labelAdd['rate']=rate

#%%  去掉borrowLeft的￥ 

borrowLeftlit=[]
borrowLeft=labelAdd['borrowLeft']
for i in borrowLeft:
    if i!='nan':
        borrowLeftlit.append(str(i)[2:])
borrowLeft=DataFrame(borrowLeftlit)         #将list转为DataFrame
labelAdd['borrowLeft']=borrowLeft

#%%  去掉badBidRadio的%
badBidRadiolit=[]
badBidRadio=labelAdd['badBidRadio']
for i in badBidRadio:
    if i!='nan':
        badBidRadiolit.append(str(i)[:-1])
badBidRadio=DataFrame(badBidRadiolit)         #将list转为DataFrame
labelAdd['badBidRadio']=badBidRadio
#%%  去掉weightedBidding InterestRate的%
weightedBidding_InterestRatelit=[]
weightedBidding_InterestRate=labelAdd['weightedBidding InterestRate']
for i in weightedBidding_InterestRate:
    if i!='nan':
        weightedBidding_InterestRatelit.append(str(i)[:-1])
weightedBidding_InterestRate=DataFrame(weightedBidding_InterestRatelit)         #将list转为DataFrame
labelAdd['weightedBidding InterestRate']=weightedBidding_InterestRate
#%%  去掉payEveryMonth的多余部分
payEveryMonthlit=[]
payEveryMonth=labelAdd['payEveryMonth']
for i in payEveryMonth:
    if i!='nan':
        payEveryMonthlit.append(str(i)[18:])
payEveryMonth=DataFrame(payEveryMonthlit)         #将list转为DataFrame
labelAdd['payEveryMonth']=payEveryMonth
print labelAdd

labelAdd.to_csv("f:/p2p/code/clear_data.csv",index=False)


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