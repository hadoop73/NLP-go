

##  词向量

**one-hot representation**

向量长度为词典的大小N,每个词的向量表示:[1,0,0,0,...,0],容易造成维数过大

**Distributed Representation**

把词映射为一个固定长度的短向量,向量之间的距离用来表示词的相似度.可以用LSA和LDA来训练词向量,或者用神经网络.


![enter description here][1]


##  CBOW 模型

把词 w 取前 c 个词和后 c 个词作为上下文,进行网络结构输入

![enter description here][2]

其中输入层和投影层

![enter description here][3]


  [1]: ./images/1491572755155.jpg "1491572755155.jpg"
  [2]: ./images/1491574657264.jpg "1491574657264.jpg"
  [3]: ./images/1491574689267.jpg "1491574689267.jpg"
