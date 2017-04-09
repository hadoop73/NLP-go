

##  Hadoop

[Hadoop 基础教程](http://blessht.iteye.com/blog/2095675)

Hadoop 的核心就是 HDFS 和 MapReduce,HDFS 也就是 Hadoop 分布式文件系统,高度容错,部署在不同的 PC 上.

[HDFS 入门](http://www.yiibai.com/hadoop/hdfs_beginners_guide.html)

**HDFS 的设计特点:**

- 大数据文件分块存储,大小可以通过hdfs-site.xml修改大小,把一个大文件分割成许多块,存储在不同主机上

- 流式数据访问,来一点处理一点,一次写入多次读写,写入的文件只能在末尾添加内容

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
# 将多个小文件合并拷贝到本地
hadoop fs -cat /user/hadoop/part-r-* > a.txt   
```

![enter description here][2]

- 客户端首先向 NameNode 读取文件块的元数据,以及数据存储地址

- 客户端再想 DataNode 读取块文件

- 读取完毕,close() 关闭连接


**HDFS 写文件:**

[HDFS的常用操作--hdfs下的文件操作常用命令总结](http://www.aboutyun.com/blog-4073-518.html)

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

[MapReduce的迭代操作](http://www.yiibai.com/spark/apache_spark_rdd.html)

![enter description here][4]


Mapreduce 是一种数据处理的编程模式.包括:**Map阶段**,**Reduce阶段**

![enter description here][5]


- map操作,对每条记录进行映射函数操作,map操作将中间结果写入本地磁盘,一旦任务完成,中间结果删除

- 对相同key的value进行操作,把结果写入到HDFS中

![enter description here][6]

- JobTrack负责作业完成,驻留在NameNode中

- TaskTrack负责作业执行,驻留在每个DataNode中


[Map-side Join和Reduce-side Join](http://blog.csdn.net/wisgood/article/details/51579264)

Map-side Join主要用于一个大文件一个小文件情况,小文件作为广播变量传送到每个工作节点,每个节点只有一份数据.避免了Spark默认的每个变量都需要发送带来的性能问题.

![enter description here][7]

其中,累加器更多的相当于一个全局变量

Reduce-side Join:先对所有的数据进行map,将相同关键词划分给同一个Reduce Task,在Reduce阶段进行合并join操作

[ spark小技巧－mapPartitions](http://blog.csdn.net/lsshlsw/article/details/48627737)

mapPartitions 主要用于对每个RDD中的分区进行操作,map 是对每个元素进行操作

#  Spark

Spark主要是进行内存集群计算,增快处理速度,中间结果保存在内存而不是磁盘中

RDD是一个不可变的带分区的记录集合,可以放在不同的节点上的分割记录集,包括两类操作:转换和动作

转换用了定义一个RDD,动作用来生成一个结果

转换操作都是惰性的,

##  RDD 分区

[Spark-RDD 分区](http://blog.csdn.net/sicofield/article/details/50983039)

RDD 是一个只读的分区记录集合,包含多个分区,每个分区是一个 dataset 片段,每个分区只能在一台机器上,RDD 的每个分区只被一个 Child RDD 的一个分区依赖,称为**窄依赖**,若一个Child RDD分区依赖多个父RDD,称为**宽依赖**.

![enter description here][8]

**区分窄依赖和宽依赖的原因**

- 宽依赖,可能会跨节点数据传输

- 失败恢复机制不同,窄依赖只需要重新计算父分区就行,而宽依赖需要计算所有的父分区

![enter description here][9]

join 操作会根据两个数据集所有键的哈希值都求出来,放在同一台机器进行join操作,数据进行了混洗,网络开销很大

如果UserData表比events表大很多,可以选择UserData进行分区,在join时候,Spark会利用这一点只需要将events混洗操作,发送到一台机器上进行join操作.

![enter description here][10]

**自定义分区**

[Spark分区HashPartitioner和RangePartitioner](https://www.iteblog.com/archives/1522.html)

在Spark内部有HashPatitioner和RangePartitioner两种分区策略,在使用Python进行自定义分区时,只需要实现关键词hash函数

```
import urlparse

def iteblog_domain(url):
  return hash(urlparse.urlparse(url).netloc)

iteblog.partitionBy(20, iteblog_domain)
```

**reduceByKey和groupByKey**

[reduceByKey和groupByKey区别与用法](http://blog.csdn.net/zongzhiyuan/article/details/49965021)

reduceByKey 会在每个RDD中进行Reduce,再shuffle,再进行Reduce性能比groupByKey好



[Spark和Hadoop对比](https://www.zhihu.com/question/26568496/answer/41608400)

**Spark解决了Hadoop的哪些问题?**

- 抽象层次低,Hadoop都是针对具体的数据自己编程处理,Spark基于RDD的抽象

- Hadoop只提供了两个操作,Map和Reduce,表达力欠缺,Spark提供了很多转换和动作,包括Join,GroupBy等

- 复杂的任务,Job之间的任务需要自己管理,在Spark中都是对RDD进行管理


## 集群安装

[Spark 1.6.1分布式集群环境搭建](https://my.oschina.net/jackieyeah/blog/659741)

```
ssh-keygen -t rsa -P ''
# 再在各个 pc 中互相拷贝密钥
# 再在每个 pc 中执行 ssh-add
```

[java.lang.IllegalArgumentException: URI has an authority component](http://stackoverflow.com/questions/37872800/hadoop2-7-0-namenode-format-java-lang-illegalargumentexception-uri-has-an-autho)


**启动Hadoop和Spark**
```
hadoop/hdfs namenode -format
hadoop/sbin/start-all.sh
spark/sbin/start-master.sh
spark/sbin/start-slaves.sh
```
**停止Hadoop和Spark**
```
spark/sbin/stop-master.sh
spark/sbin/stop-slaves.sh
hadoop/sbin/stop-all.sh
```


##  Spark 集群

Spark 集群采用主从结构,一个节点负责中央协调,调度各个分布式工作节点,这个中央节点称为**驱动器节点**.工作节点称为**执行器节点**.驱动器节点和执行器节点一起被称为**Spark应用**


![enter description here][11]

驱动器节点通过集群管理器对执行器节点进行管理,尝试把所有任务基于数据所在位置分配给合适的执行器进程.

执行器功能:执行任务,存储RDD数据


```
# 查看Spark Jobs完成情况
http://master:4040/
# 查看Spark集群情况
http://master:8080/
```


###  Spark DataFrame

[从CSV文件读取到DataFrame中](https://www.nodalpoint.com/spark-dataframes-from-csv-files/)

[RDD、DataFrame和DataSet的区别](http://www.jianshu.com/p/c0181667daa0)

DataFrame比RDD拥有更丰富的结构信息,列名称和类型等信息

DataFrame是ROW对象的集合,更加丰富的算子,还包括列信息能够优化查询

RDD强调不变性,会产生大量临时对象,对GC造成压力

DataSet每个记录是一个强类型

##  SparkContext和SparkSession

[Spark 2.0系列之SparkSession详解](http://www.raincent.com/content-85-7196-1.html)

![enter description here][12]

SparkSession 是2.0引入,统一的Spark切入点,更能更加丰富包含DataFrame和DataSet等API

SparkContext是使用其他Spark功能的中介,driver通过SparkContext连接到集群管理器对任务进行控制

[Spark SQL, DataFrames 以及 Datasets 编程指南](http://ifeve.com/spark-sql-dataframes/)


  [1]: ./images/1490786580554.jpg "1490786580554.jpg"
  [2]: ./images/1490787242620.jpg "1490787242620.jpg"
  [3]: ./images/1490787885680.jpg "1490787885680.jpg"
  [4]: ./images/1490887381651.jpg "1490887381651.jpg"
  [5]: ./images/1490788559148.jpg "1490788559148.jpg"
  [6]: ./images/1490791468451.jpg "1490791468451.jpg"
  [7]: ./images/1491344613331.jpg "1491344613331.jpg"
  [8]: ./images/1490891412109.jpg "1490891412109.jpg"
  [9]: ./images/1490891742075.jpg "1490891742075.jpg"
  [10]: ./images/1490891940921.jpg "1490891940921.jpg"
  [11]: ./images/1490960489315.jpg "1490960489315.jpg"
  [12]: ./images/1490993876637.jpg "1490993876637.jpg"
