

##  Hadoop

[Hadoop 基础教程](http://blessht.iteye.com/blog/2095675)

Hadoop 的核心就是 HDFS 和 MapReduce,HDFS 也就是 Hadoop 分布式文件系统,高度容错,部署在不同的 PC 上.

[HDFS 入门](http://www.yiibai.com/hadoop/hdfs_beginners_guide.html)

**HDFS 的设计特点:**

- 大数据文件分块存储,把一个大文件分割成许多块,存储在不同主机上

- 流式数据访问,一次写入多次读写,写入的文件只能在末尾添加内容

- 硬件故障处理,为了防止某个主机的分块文件失效,它将分块的副本保存在多个主机上

**HDFS 组成元素:**

- Block:文件分块,通常 64M

- NameNode:保存完整的文件系统目录信息,文件信息以及分块信息,由一台主机负责

- DataNode:存储 Block 块文件


![enter description here][1]


**HDFS 读文件**

```
# 将 temp.txt 拷贝到本地文件系统
hdfs dfs -copyToLocal /temp.txt
```

![enter description here][2]

- 客户端首先向 NameNode 读取文件块的元数据,以及数据存储地址

- 客户端再想 DataNode 读取块文件

- 读取完毕,close() 关闭连接


**HDFS 写文件:**

```
# 从本地文件系统中拷贝 temp.txt 到 HDFS 中
hdfs dfs -copyFromLocal temp.txt /
```

![enter description here][3]

- 先向 NameNode 请求写文件,NameNode验证文件名是否冲突,用户是否有权限

- NameNode 返回一条记录,客户端使用它来写数据到 HDFS

- 数据被写入到 DataQueue 中,再由 DataStreamer 组件消耗 DataQueue


##  MapReduce

[MapReduce 简单入门](http://www.yiibai.com/hadoop/intro-mapreduce.html)

Mapreduce 是一种数据处理的编程模式.包括:**Map阶段**,**Reduce阶段**

![enter description here][4]


- map操作,对每条记录进行映射函数操作,map操作将中间结果写入本地磁盘,一旦任务完成,中间结果删除

- 对相同key的value进行操作,把结果写入到HDFS中

![enter description here][5]

- JobTrack负责作业完成,驻留在NameNode中

- TaskTrack负责作业执行,驻留在每个DataNode中



#  Spark

Spark主要是进行内存集群计算,增快处理速度

RDD是一个不可变的带分区的记录集合,包括两类操作:转换和动作

转换用了定义一个RDD,动作用来生成一个结果

转换操作都是惰性的,


[Spark和Hadoop对比](https://www.zhihu.com/question/26568496/answer/41608400)

**Spark解决了Hadoop的哪些问题?**

- 抽象层次低,Hadoop都是针对具体的数据自己编程处理,Spark基于RDD的抽象

- Hadoop只提供了两个操作,Map和Reduce,表达力欠缺,Spark提供了很多转换和动作,包括Join,GroupBy等

- 复杂的任务,Job之间的任务需要自己管理,在Spark中都是对RDD进行管理























  [1]: ./images/1490786580554.jpg "1490786580554.jpg"
  [2]: ./images/1490787242620.jpg "1490787242620.jpg"
  [3]: ./images/1490787885680.jpg "1490787885680.jpg"
  [4]: ./images/1490788559148.jpg "1490788559148.jpg"
  [5]: ./images/1490791468451.jpg "1490791468451.jpg"
