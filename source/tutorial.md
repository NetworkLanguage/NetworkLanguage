## 安装环境及代码使用说明

### 安装环境

- Python 3 +
- Pytorch 1.1
- Pandas
- Numpy
- jieba
- tqdm
- sklearn
- gensim
- fasttext
- tensorboard



### 使用说明

#### 数据集选择

在每个方法对应的代码中取消注释以选择相应的数据集

```python
# task = "weibo_gender"
# task = "weibo_area"
task = "douban"
```


#### BOW

- [code](https://github.com/NetworkLanguage/NetworkLanguage/blob/master/python_codes/bow.py)


- 训练并测试

```python
python bow.py
```



#### Word2vec

- [code](https://github.com/NetworkLanguage/NetworkLanguage/blob/master/python_codes/w2v.py)

- main函数中可调整参数有：
	- dim: 词向量维度
	- iter: word2vec训练迭代次数

- 训练并测试
```python
python w2v.py
```



#### fastText

- [code](https://github.com/NetworkLanguage/NetworkLanguage/blob/master/python_codes/fast_text.py)

- main函数可调整参数有：
    - dim: 特征维度
    - epoch：模型训练迭代次数

- 训练并测试
```python
python fast_text.py
```



#### BERT与ERNIE

- [BERT code](https://github.com/NetworkLanguage/NetworkLanguage/blob/master/python_codes/Bert/models/bert.py)
- [ERNIE code](https://github.com/NetworkLanguage/NetworkLanguage/blob/master/python_codes/Bert/models/ERNIE.py)

- 训练并测试

```python
# bert
python run.py --model bert
# ERNIE
python run.py --model ERNIE
```