### 关于本项目
本项目为2020年中国高校计算机大赛(C4)－网络技术挑战赛EP2赛项，题目为构建一个在线流量识分析与识别系统，能够实时识别出网络上的正常业务流量、恶意软件流量和网络攻击流量，并对各种流量随时序的变化进行进行可视化展示，我们在XGboost模型的基础上使用Stacking集成学习技术，将思博伦官方给出的流量pcap包解析为流量的URL进行训练, 最终在官方给出的测试流量包上达到92%的准确率


### 环境配置
Python (3.6)  
numpy (1.19.5)  
pandas (1.1.5)  
scikit-learn (0.24.1)  
joblib (1.0.1)  



### 数据集
我们的数据读取和预处理(TF-IDF编码)逻辑由在process.py模块完成
训练所用的数据集采用赛方提供的pcap包数据集，已经经过Scapy的解析将流量的URL提取出来，放在项目目录中的data文件夹下，三种类型的流量分别存放为和业务流量.csv、恶意软件.csv、网络攻击.csv  
因为我们采用的是线上实时分析系统，线上实时测试数据需要从MySQL数据库中读取，经过模型的推断后再在前端可视化呈现。我们这里为了方便已经将MySQL中的已经经过Scapy解析的URL流量数据提取出来存放在data目录下，将流量内容和时间戳分别保存为时间戳.csv和测试流量.csv  

### 特征工程
特征工程逻辑由feature.py模块完成，详情可阅读项目介绍PDF文档

### 模型
我本地训练的模型已经保存在model目录下，可直接进行测试

### 模型交叉验证与线上推断

运行:
```
main.py
```
上线后的代码是从MySQL中读取测试数据集，这里为了方便我们已经将经过Scapy解析的测试数据集放在data目录下，可以直接运行测试
