# coding:utf-8



from pyspark import SparkContext,SparkConf
import numpy as np

import os
os.environ["SPARK_HOME"] = "/home/hadoop/spark-2.0.1-bin-hadoop2.7"   #KeyError: 'SPARK_HOME'
conf = SparkConf()
sc=SparkContext(appName='t5',conf=conf)

data = sc.textFile('file:///home/hadoop/PycharmProjects/NLP/spark/data/5')

import sys

def f(x):
    mi = sys.maxint
    ma = -sys.maxint
    for xi in x[1]:
        mi = min(xi,mi)
        ma = max(xi,ma)
    return (ma,mi)

res = data.filter(lambda x:len(x.strip())>0) \
          .map(lambda x:('Key',int(x.strip()))) \
          .groupByKey() \
          .map(f) \
          .collect()

print res

print "max: ",res[0][0]
print "min: ",res[0][1]




