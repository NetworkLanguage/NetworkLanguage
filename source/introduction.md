## 项目介绍

本项目为**网络语言特征刻画与身份识别方法研究**项目，旨在从网络语言文本数据中抽取特征，并基于机器学习方法与深度学习方法实现对用户身份的识别。本项目在两个中文文本数据集上展开了实验，分别是新浪微博用户短文本数据集与豆瓣影评数据集。在新浪微博数据集上，本项目基于用户所发布的短文本数据实现了对用户的性别（男性或女性）及地区（华东、华南、华北、华中、西南、西北、东北、港澳台、海外、其他等）的预测；在豆瓣影评数据集上，本项目基于某条影评文本数据预测了它的发布者身份。

本项目在两个数据集上采用了以下方法建立模型：

- BOW

- Word2vec

- fastText

- BERT

- ERNIE

（其中BERT与ERNIE模型参照了GitHub仓库：[Bert-Chinese-Text-Classification-Pytorch](https://github.com/649453932/Bert-Chinese-Text-Classification-Pytorch)）

整体框架如下图所示：

<img src="https://gitee.com/networklanguage/NetworkLanguage/raw/master/images/framework.png" style="zoom:30%" />

&nbsp;

