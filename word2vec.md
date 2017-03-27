
# word2vec 数学原理



word2vec 是 Google 于 2013 年开源的 word vector 工具包,简单高效.



##  sigmoid 函数

  sigmoid 函数是神经网络中常用的激活函数之一。定义为:

![enter description here][1]


![enter description here][2]

![enter description here][3]



##  逻辑回归

二分类的 hypothesis 函数利用 sigmoid 函数,对于任意样本![enter description here][4]可以定义为:

![enter description here][5]


把样本扩充![enter description here][6]所以假设函数可以定义如下

![enter description here][7]

对于假设函数的参数求值,可以先定义一个整体损失函数

![enter description here][8]


![enter description here][9]


![enter description here][10]


##  统计语言模型

统计语言模型是用来计算一个句子概率的**概率模型**.


###  n-gram 模型



![enter description here][11]

n-gram 模型假设一个词的出现只与前面几个词有关.因此上面的公式可以改写为


![enter description here][12]

模型参数 n 的选择需要考虑词典大小,一般来说 n 越大模型越复杂,实际应用 n = 3


###  神经概率语言模型






  [1]: ./images/1490615146270.jpg "1490615146270.jpg"
  [2]: ./images/1490616454318.jpg "1490616454318.jpg"
  [3]: ./images/1490616498592.jpg "1490616498592.jpg"
  [4]: ./images/1490617157688.jpg "1490617157688.jpg"
  [5]: ./images/1490617181380.jpg "1490617181380.jpg"
  [6]: ./images/1490617220355.jpg "1490617220355.jpg"
  [7]: ./images/1490617250125.jpg "1490617250125.jpg"
  [8]: ./images/1490617405809.jpg "1490617405809.jpg"
  [9]: ./images/1490617573403.jpg "1490617573403.jpg"
  [10]: ./images/1490617627776.jpg "1490617627776.jpg"
  [11]: ./images/1490619319085.jpg "1490619319085.jpg"
  [12]: ./images/1490619442283.jpg "1490619442283.jpg"
