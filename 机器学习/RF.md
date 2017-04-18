
#  随机森林

[ Random Forest（sklearn参数详解)](http://blog.csdn.net/u012102306/article/details/52228516)

- n_estimators：决策树的个数
- criterion：分支指标
- max_features：属性选择时，最大的特征选择数
if “auto”, then max_features=sqrt(n_features).
If “sqrt”, thenmax_features=sqrt(n_features).
If “log2”, thenmax_features=log2(n_features).
If None, then max_features=n_features.


##  随机森林生成过程

![enter description here][1]

每次生成一棵树的时候，会 Boostrap 抽样 n 个样本作为训练数据，并随机抽取 m 个特征 max_features 个特征，进行训练
训练时候，通过 gini 指数来进行分支判断，最后结果：分类用投票作为最后的结果；回归使用均值作为最后的结果。

##  剪枝


  [1]: ./images/1492449688548.jpg "1492449688548"