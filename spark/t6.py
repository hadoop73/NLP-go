# coding:utf-8



from pyspark import SparkContext,SparkConf
import numpy as np

import os
os.environ["SPARK_HOME"] = "/home/hadoop/spark-2.0.1-bin-hadoop2.7"   #KeyError: 'SPARK_HOME'
conf = SparkConf()
sc=SparkContext(appName='t5',conf=conf)

data = sc.textFile('file:///home/hadoop/PycharmProjects/NLP/spark/data/6')

"""
1,9819,100,121

#orderid,userid,payment,productid
求topN的payment值
"""
res = data.filter(lambda x:len(x.strip())>0)\
        .map(lambda x:int(x.split(',')[2])) \
        .sortBy(lambda x:-x) \
        .zipWithIndex() \
        .map(lambda x:(x[1],x[0])) \
        .take(5) \


print res


