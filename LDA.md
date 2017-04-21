


[Markdown 数学公式](http://oiltang.com/2014/05/04/markdown-and-mathjax/)

#  LDA

[LDA算法理解](https://www.zybuluo.com/Dounm/note/435982#fnref:1)

LDA 图模型表示如下所示：

 ![enter description here][1]


LDA 的两个过程：

- 第一个过程，生成文本的 doc-topic 骰子，用来生成文档的主题编号。

- 第二个过程，通过主题编号来确定 topic-word 骰子，再用这个骰子生成 word。

因为文档在主题上式一个分布，所以需要先选定一个主题，而每个主题是由词组成的，所以再从词组中抽取词来生成文档

![enter description here][2]



主题-词的联合概率分布:

![enter description here][3]

m表示第m篇文档,k表示第k个主题



## 多项式分布



>在 $ A_1,A_2,...,A_n $ 的完备事件群中，事件两两互斥，其中 $ A_1,A_2,...,A_n $ 的概率分别是$ p_1,p_2,...,p_n $。将事件独立重复N次,$X_i$ 表示N次试验中事件$A_i$ 出现的次数，则$ X = (X_1,X_2,...,X_n)$ 是n维随机变量，X的概率分布就是多项分布，联合概率为：
![enter description here][4]

![enter description here][5]


### Gamma 函数

Gamma 函数将阶乘扩展到正实数域内。

![enter description here][6]

### Beta 分布



![enter description here][7]

使用B(a,b)替换分母，则Beta 分布可以表示为以下形式

![enter description here][8]

Beta 分布的期望为$\frac{\alpha}{\alpha+\beta}$

![enter description here][9]


###  狄里克雷分布

![enter description here][10]

狄里克雷的期望

![enter description here][11]

##  共轭分布

![enter description here][12]

二项分布和Beta分布互为共轭分布

![enter description here][13]

Dirichlet 分布式多项式的共轭先验分布

![enter description here][14]


  [1]: ./images/1492566242535.jpg "1492566242535"
  [2]: ./images/1492566614711.jpg "1492566614711"
  [3]: ./images/1490704249596.jpg "1490704249596.jpg"
  [4]: ./images/1492609893411.jpg "1492609893411"
  [5]: ./images/1492610096088.jpg "1492610096088"
  [6]: ./images/1492610302591.jpg "1492610302591"
  [7]: ./images/1492610869530.jpg "1492610869530"
  [8]: ./images/1492611091602.jpg "1492611091602"
  [9]: ./images/1492611759631.jpg "1492611759631"
  [10]: ./images/1492611878757.jpg "1492611878757"
  [11]: ./images/1492611950110.jpg "1492611950110"
  [12]: ./images/1492612241212.jpg "1492612241212"
  [13]: ./images/1492614104039.jpg "1492614104039"
  [14]: ./images/1492614557267.jpg "1492614557267"