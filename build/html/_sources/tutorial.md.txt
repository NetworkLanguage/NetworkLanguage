## 安装环境及运行
### 环境需求

1. Python版本及环境

   Python 3.6

2. 安装包

   - scikit-learn 0.21.3
   - gensim 3.8.0
   - jieba 0.39
   - fasttext 0.9.1

### 运行

1. BOW（词袋模型）

   

2. Word2vec

   - 代码见

   - main函数中可调整参数有：
     - task: 对应三个预测任务，分别为weibo_gender, weibo_area, douban
     - dim: 词向量维度
     - iter: word2vec训练迭代次数

3. fastText

   - 代码见

   - main函数可调整参数有：
     - task: 对应三个预测任务，分别为weibo_gender, weibo_area, douban
     - dim: 特征维度
     - epoch：模型训练迭代次数

4. BERT

5. ERNIE

