
#  随机森林

[ Random Forest（sklearn参数详解)](http://blog.csdn.net/u012102306/article/details/52228516)

- n_estimators：决策树的个数
- criterion：分支指标
- max_features：属性选择时，最大的特征选择数

> if “auto”, then max_features=sqrt(n_features).
If “sqrt”, thenmax_features=sqrt(n_features).
If “log2”, thenmax_features=log2(n_features).
If None, then max_features=n_features.


##  随机森林生成过程

![enter description here][1]

每次生成一棵树的时候，会 Boostrap 抽样 n 个样本作为训练数据，并随机抽取 m 个特征 max_features 个特征，进行训练
训练时候，通过 gini 指数来进行分支判断，最后结果：分类用投票作为最后的结果；回归使用均值作为最后的结果。

##  剪枝

决策树剪枝往往通过极小化决策树的损失函数，损失函数考虑了叶节点个数，以及叶节点的熵

![enter description here][2]


**信息增益**

**熵** 表示随机变量不确定性的度量，设 X 是一个取有限值的离散随机变量，概率分布为：

![enter description here][3]

随机变量 X 的熵定义为：

![enter description here][4]

对于二分类问题，X 的取值就是 0,1 训练结果就是使得 X 取值相同的尽量在同一个分支来减少熵。

**条件熵 H(Y|X)** 表示在已知随机变量X的条件下Y的不确定性。定义为X给定条件下Y的条件概率分布的熵对X的数学期望：

![enter description here][5]

**信息增益** 特征A对训练数据D的信息增益 g(D,A)，定义为集合D的经验熵H(D)与特征A给定条件下的条件熵之差。

![enter description here][6]

损失函数由两部分组成，第一部分表示模型对训练数据的预测误差，第二部分表示决策树的复杂度，通过 α 来调整两者的平衡

![enter description here][7]


**信息增益比**

[c4.5为什么使用信息增益比来选择特征？](https://www.zhihu.com/question/22928442)

由于在训练数据某些特征的取值比较多，则信息增益值也会偏大，比如用户的信用卡id，按照id来对违约进行判断时，经验熵为0，信息增益很大，但是用户信用卡id并不能用来作为特征进行训练，为了克服这种问题，

![enter description here][8]

考虑 Info 的划分带来的信息，

![enter description here][9]


##  ID3 算法

决策树按照信息增益进行分枝，直到信息增益很小或者没有信息增益为止

##  C4.5 算法

按照信息增益比来生成决策树

## CART 算法

CART 算法由两步组成：

- 决策树生成

- 决策树剪枝

**决策树生成**

对回归树用平方误差最小化准则，对分类树用基尼指数最小化准则。

回归树进行分枝的时候，选择一个变量和一个切分点，并计算两个区域的平方误差和。选择最小的平方误差和作为分枝，一直到满足停止条件。

![enter description here][10]

分类树通过基尼指数来选择最优特征和最优切分点。

![enter description here][11]

分枝时候的基尼指数，选择最小的基尼指数作为分枝

![enter description here][12]

**CAER剪枝**


  [1]: ./images/1492449688548.jpg "1492449688548"
  [2]: ./images/1492522554921.jpg "1492522554921"
  [3]: ./images/1492503474449.jpg "1492503474449"
  [4]: ./images/1492504920229.jpg "1492504920229"
  [5]: ./images/1492505249709.jpg "1492505249709"
  [6]: ./images/1492505520321.jpg "1492505520321"
  [7]: ./images/1492522641209.jpg "1492522641209"
  [8]: ./images/1492522045248.jpg "1492522045248"
  [9]: ./images/1492522080091.jpg "1492522080091"
  [10]: ./images/1492523824746.jpg "1492523824746"
  [11]: ./images/1492523872066.jpg "1492523872066"
  [12]: ./images/1492523924057.jpg "1492523924057"