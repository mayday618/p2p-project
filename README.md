# p2p-project
现在开始用GitHub保管我的P2P项目代码
# 总体说明
* 数据集包括p2p网站[拍拍贷](http://www.ppdai.com/)的用户信息（usr.csv）,借款信息（bid.csv）,投标信息（record.csv）,还款信息（otherinfo.csv）
* 将数据集分为训练集和测试集
* 特征信息（X）为bid和usr的合并 标签信息（y）为是否还款成功
* 将此问题视为典型的二分类问题 可运用分类算法进行预测  并计算预测效果
# 过程说明
将其视为机器学习的过程 包括典型的流程
1. 数据合并
2. 数据可视化分析 
3. 数据预处理
4. 特征工程
5. 数据划分为训练集和测试集
6. 基本分类模型预测
7. 集成模型预测
# 数据集
data/origin_data存放原始数据
* user文件夹存用户信息
* bid.csv借款信息
* record.csv投标信息
* otherinfo.csv还款信息
data/merge_data存放融合之后的数据
* allUser.csv对所有user.csv进行合并生成的全部用户信息
* label.csv从record.csv中提取的还款成功与否信息
# 数据清洗
文件夹clear进行数据的清洗
clear/number_clear进行在字符串中提取中数字 保存到clear_data.csv中
clear/category.py 进行类别型信息的映射
# 数据合并
文件夹merge存将origin_data进行合并的py代码

