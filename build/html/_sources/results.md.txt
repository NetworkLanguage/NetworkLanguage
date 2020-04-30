### 实验结果

该部分展示不同模型方法在不同任务中的表现效果，使用的指标有Precision，Recall， F1  



#### 根据微博文本预测用户性别

<table border="1" cellpadding="10">
    <tr>
        <th colspan = "2" align="center">model</th>
        <th align="center">Precision</th>
        <th align="center">Recall</th>
        <th align="center">  F1  </th>
    </tr>
    <tr>
        <td rowspan = "4" valign="middle"><b>BOW</b></td>
        <td align="center">逻辑回归</td>
        <td align="center">0.6875</td>
        <td align="center">0.6868 </td>
        <td align="center">0.6810 </td>
    </tr>
    <tr>
        <td align="center">支持向量机</td>
        <td align="center">0.6685 </td>
        <td align="center">0.6701 </td>
        <td align="center">0.6671 </td>
    </tr>
    <tr>
        <td align="center">随机森林</td>
        <td align="center">0.6724 </td>
        <td align="center">0.6740 </td>
        <td align="center">0.6737 </td>
    </tr>
    <tr>
        <td align="center">神经网络</td>
        <td align="center">0.6576 </td>
        <td align="center">0.6592 </td>
        <td align="center">0.6577 </td>
    </tr>
    <tr>
        <td rowspan = "4" valign="middle"><b>Word2vec</b></td>
        <td align="center">逻辑回归</td>
        <td align="center">0.6795</td>
        <td align="center">0.6810</td>
        <td align="center">0.6789</td>
    </tr>
    <tr>
        <td align="center">支持向量机</td>
        <td align="center">0.6715</td>
        <td align="center">0.6730</td>
        <td align="center">0.6700</td>
    </tr>
    <tr>
        <td align="center">随机森林</td>
        <td align="center">0.6657</td>
        <td align="center">0.6672</td>
        <td align="center">0.6657</td>
    </tr>
    <tr>
        <td align="center">神经网络</td>
        <td align="center">0.6718</td>
        <td align="center">0.6722</td>
        <td align="center">0.6667</td>
    </tr>
    <tr>
        <td colspan = "2" align="center"><b>fastText</b></td>
        <td align="center"><b>0.6899</b></td>
        <td align="center"><b>0.6911</b></td>
        <td align="center"><b>0.6899</b></td>
    </tr>
    <tr>
        <td colspan = "2" align="center"><b>BERT</b></td>
        <td align="center">0.6709 </td>
        <td align="center">0.6628 </td>
        <td align="center">0.6471 </td>
    </tr>
    <tr>
        <td colspan = "2" align="center"><b>ERNIE</b></td>
        <td align="center">0.6894</td>
        <td align="center">0.6897</td>
        <td align="center">0.6895</td>
    </tr>
</table>
&nbsp;



#### 根据微博文本预测用户所在地区

 考虑到用户的省份较多，且部分用户集中在北京、上海、广州等地，其他省份的用户数量较少。因此根据地理位置分布，将用户所在省份划分为**华北、华东、华南、华中、东北、西北、西南、港澳台地区、海外**这9个区域，并预测用户所在的区域。  

<table border="1" cellpadding="10">
    <tr>
        <th colspan = "2" align="center">model</th>
        <th align="center">Precision</th>
        <th align="center">Recall</th>
        <th align="center">  F1  </th>
    </tr>
    <tr>
        <td rowspan = "4" valign="middle"><b>BOW</b></td>
        <td align="center">逻辑回归</td>
        <td align="center">0.3868</td>
        <td align="center">0.4065</td>
        <td align="center">0.3204</td>
    </tr>
    <tr>
        <td align="center">支持向量机</td>
        <td align="center">0.4422 </td>
        <td align="center">0.4313 </td>
        <td align="center">0.3724</td>
    </tr>
    <tr>
        <td align="center">随机森林</td>
        <td align="center">0.3642</td>
        <td align="center">0.3833 </td>
        <td align="center">0.2905 </td>
    </tr>
    <tr>
        <td align="center">神经网络</td>
        <td align="center">0.4077</td>
        <td align="center">0.4189 </td>
        <td align="center">0.3836 </td>
    </tr>
    <tr>
        <td rowspan = "4" valign="middle"><b>Word2vec</b></td>
        <td align="center">逻辑回归</td>
        <td align="center">0.3811</td>
        <td align="center">0.4211</td>
        <td align="center">0.3754</td>
    </tr>
    <tr>
        <td align="center">支持向量机</td>
        <td align="center">0.3713</td>
        <td align="center">0.3876</td>
        <td align="center">0.2776</td>
    </tr>
    <tr>
        <td align="center">随机森林</td>
        <td align="center">0.3926</td>
        <td align="center">0.4153</td>
        <td align="center">0.3460</td>
    </tr>
    <tr>
        <td align="center">神经网络</td>
        <td align="center">0.3789</td>
        <td align="center">0.4073</td>
        <td align="center">0.3746</td>
    </tr>
    <tr>
        <td colspan = "2" align="center"><b>fastText</b></td>
        <td align="center">0.4048</td>
        <td align="center">0.4204</td>
        <td align="center">0.4035</td>
    </tr>
    <tr>
        <td colspan = "2" align="center"><b>BERT</b></td>
        <td align="center">0.1129</td>
        <td align="center">0.3360 </td>
        <td align="center">0.1690 </td>
    </tr>
    <tr>
        <td colspan = "2" align="center"><b>ERNIE</b></td>
        <td align="center"><b>0.4689</b></td>
        <td align="center"><b>0.4735</b></td>
        <td align="center"><b>0.4484</b></td>
    </tr>
</table>
&nbsp;

#### 根据豆瓣影评预测用户

<table border="1" cellpadding="10">
    <tr>
        <th colspan = "2" align="center">model</th>
        <th align="center">Precision</th>
        <th align="center">Recall</th>
        <th align="center">  F1  </th>
    </tr>
    <tr>
        <td rowspan = "3" valign="middle"><b>BOW</b></td>
        <td align="center">逻辑回归</td>
        <td align="center">0.1585 </td>
        <td align="center"><b>0.1354</b></td>
        <td align="center"><b>0.1073</b></td>
    </tr>
    <tr>
        <td align="center">朴素贝叶斯</td>
        <td align="center"><b>0.1835</b></td>
        <td align="center">0.1093 </td>
        <td align="center">0.0892</td>
    </tr>
    <tr>
        <td align="center">神经网络</td>
        <td align="center">0.1096</td>
        <td align="center">0.0689 </td>
        <td align="center">0.0775 </td>
    </tr>
    <tr>
        <td rowspan = "3" valign="middle"><b>Word2vec</b></td>
        <td align="center">逻辑回归</td>
        <td align="center">0.0606</td>
        <td align="center">0.0773</td>
        <td align="center">0.0614</td>
    </tr>
    <tr>
        <td align="center">朴素贝叶斯</td>
        <td align="center">0.0366</td>
        <td align="center">0.0491</td>
        <td align="center">0.0321</td>
    </tr>
    <tr>
        <td align="center">神经网络</td>
        <td align="center">0.0572</td>
        <td align="center">0.0753</td>
        <td align="center">0.0563</td>
    </tr>
    <tr>
        <td colspan = "2" align="center"><b>fastText</b></td>
        <td align="center">0.1112</td>
        <td align="center">0.1014</td>
        <td align="center">0.0965</td>
    </tr>
    <tr>
        <td colspan = "2" align="center"><b>BERT</b></td>
        <td align="center">0</td>
        <td align="center">0.0023 </td>
        <td align="center">0 </td>
    </tr>
    <tr>
        <td colspan = "2" align="center"><b>ERNIE</b></td>
        <td align="center">0</td>
        <td align="center">0.0013</td>
        <td align="center">0</td>
    </tr>
</table>
   

&nbsp;

#### 结果分析
一般而言，通过深度方法的词表示学习能够获得表征词之间相似性的向量表示，因此较新的深度学习模型在文本分类任务中表现更优。
通过以上3个问题的实验结果，我们总结了一些新的发现：
- 对性别/地区的预测，和普遍认知相同，深度学习方法相对来说有较大提升。
- 在对人的身份id的识别中，深度学习的方法表现效果不好。这说明可能一个人的用词习惯是固定的，在同一类词中一个人可能只偏好使用某个词语。由此，发现词之间的关联性对个人id的预测帮助不大。

因此，对于不同的任务，不同方法的效果也会存在差距，需要结合具体问题做进一步分析。