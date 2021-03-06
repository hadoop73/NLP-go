##  隐马尔可夫模型


**隐马尔可夫模型**描述了由隐马尔科夫链生成不可观测状态,再由各个状态生成可观测的随机序列的过程.中间生成的不可观察序列称为**状态序列**,每个状态序列再生成一个随机观测序列,称为**观测序列**.

隐马尔可夫模型由**初始概率分布**,**状态转移概率分布**以及**观测概率分布**确定.

![enter description here][1]


**状态转移概率分布**描述了时刻t处于q状态,而在t+1时刻转移到状态p的概率

![enter description here][2]

![enter description here][3]

![enter description here][4]

隐马尔可夫模型的两个基本假设

- 齐次马尔科夫假设,任意时刻的状态只依赖与前一时刻的状态,与其他时刻的状态及观测无关

![enter description here][5]


- 观察独立性假设,任意时刻的观测只依赖于该时刻的马尔科夫链的状态,与其他观测及状态无关

![enter description here][6]


**隐马尔可夫模型3个基本问题**

- 概率计算问题.给定模型与观测序列,计算初始模型下,观测序列的概率

- 学习问题.已知观测序列,估计初始模型参数,使得最大似然估计最大

- 预测问题,即解码问题.已知初始模型参数和观测序列,求最有可能的状态序列

![enter description here][7]



##  维特比算法

目标是为了解码状态序列,通过最大化单个路径概率,并找出状态序列

![enter description here][8]


![enter description here][9]

通过T个时间步求出每个步状态为端点的最大路径概率,并保存此时的前一个状态,到了最后的状态,再回溯就能够获得最大路径



  [1]: ./images/1491229614555.jpg "1491229614555.jpg"
  [2]: ./images/1491229150235.jpg "1491229150235.jpg"
  [3]: ./images/1491229187769.jpg "1491229187769.jpg"
  [4]: ./images/1491229221811.jpg "1491229221811.jpg"
  [5]: ./images/1491229509170.jpg "1491229509170.jpg"
  [6]: ./images/1491229752694.jpg "1491229752694.jpg"
  [7]: ./images/1491230206800.jpg "1491230206800.jpg"
  [8]: ./images/1491235849784.jpg "1491235849784.jpg"
  [9]: ./images/1491235948611.jpg "1491235948611.jpg"
