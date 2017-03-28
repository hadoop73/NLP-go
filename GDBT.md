

# GBDT

[GBDT of Data Mining](https://zhuanlan.zhihu.com/p/25705586)

GBDT 有三部分组成:Regression Decision Tree,Gradient Boosting,Shrinkage


## DT:回归树 Regression Decision Tree

回归树用于实数值预测,分类树用于标签值预测;GBDT 的核心就是累加每棵树的预测结果

回归树是以最小化均方差为目标进行分支,分支后每个节点的值为当前节点的均值.


## GB:梯度迭代

[GBDT的梯度提升过程](https://zhuanlan.zhihu.com/p/25805870)

迭代减少残差,第一棵树会训练得到一个残差,第二颗数则以残差作为目标值进行训练,每棵树都是以上一颗树的残差为目标进行训练.比如A的年龄是10岁,第一棵树训练认为年龄为6岁,则第二颗数以残差4岁为目标进行训练.

而在很多的数据对象时,残差用负梯度来拟合,再用下一颗决策树来减小



#  XGBoost

首先改写了目标函数,把目标函数用一阶和二阶泰勒展开式表示.

![enter description here][1]


XGBoost 与 GBDT 的区别在于,目标函数不同

在 GBDT 中只有用到了负梯度作为下一颗树的目标函数

XGBoost 用到了二阶泰勒展开式

另外,XGBoost 中每一颗训练树都加入了正则项

![enter description here][2]

训练过程也不一样,XGBoost 采用了贪心算法去逼近,最后的叶子节点

![enter description here][3]

![enter description here][4]

而 GBDT 每一次分支,就是使得目标函数最小化


![enter description here][5]


  [1]: ./images/1490686707956.jpg "1490686707956.jpg"
  [2]: ./images/1490686891896.jpg "1490686891896.jpg"
  [3]: ./images/1490687063297.jpg "1490687063297.jpg"
  [4]: ./images/1490687025271.jpg "1490687025271.jpg"
  [5]: ./images/1490687430643.jpg "1490687430643.jpg"
