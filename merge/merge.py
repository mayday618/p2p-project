import pandas as pd


bid = pd.read_csv("f:/p2p/p2p-project/data/origin_data/bid.csv",error_bad_lines=False)    #读取特征文件
user = pd.read_csv("f:/p2p/p2p-project/data/merge_data/allUser.csv",error_bad_lines=False)   #读取用户信息
label = pd.read_csv("f:/p2p/p2p-project/data/merge_data/label.csv",error_bad_lines=False)    #读取标签信息


