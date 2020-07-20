from process import readFile
from feature import get_top_n_features
from model import train
import pandas as pd
import numpy as np
if __name__ =='__main__':
    #读取训数据并构建训练集特征矩阵，训练集标签，测试集特征矩阵
    X_train,Y_train,X_test=readFile()
    
    #获取top30的特征对应的下标
    feature_top_n, feature_importance = get_top_n_features(X_train, Y_train, 30)
    
    #用筛选出的特征重新构建训练集和测试集
    X_train = pd.DataFrame(X_train[feature_top_n])
    X_test = pd.DataFrame(X_test[feature_top_n])

    #模型训练与交叉验证
    gbm,x_train,x_test=train(X_train,Y_train,X_test)

    #模型推断并写入结果
    predictions = gbm.predict(x_test)
    id=np.arange(0,len(predictions),1)
    StackingSubmission = pd.DataFrame({'ID':id,'label': predictions}) 
    StackingSubmission.to_csv('./data/testy.csv',index=False,sep=',') 
	
    #按照原本的训练集进行推断查看精度
    #进行推断
    y_hat=gbm.predict(x_train)
    #打印结果
    tot=r=0
    for url , y,y_hat in zip(x_train,np.array(Y_train),y_hat):
        if y ==  y_hat:
            r=r+1
        tot=tot+1
    print("准确度:%f"%(r/tot))
        
