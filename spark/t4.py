# coding:utf-8



from pyspark import SparkContext,SparkConf
import numpy as np

import os
os.environ["SPARK_HOME"] = "/home/hadoop/spark-2.0.1-bin-hadoop2.7"   #KeyError: 'SPARK_HOME'
conf = SparkConf()
sc=SparkContext(appName='t4',conf=conf)

data = sc.textFile('file:///home/hadoop/PycharmProjects/NLP/spark/data/4')

import re
p = re.compile('\s+')


res = data.filter(lambda x:len(x.strip())>0) \
    .map(lambda line:(p.split(line.strip())[0],int(p.split(line.strip())[1])) ) \
    .combineByKey((lambda x: (x, 1)),
                  (lambda x, y: (x[0] + y, x[1] + 1)),
                  (lambda x, y: (x[0] + y[0], x[1] + y[1]))) \
    .mapValues(lambda xy:1.0 * xy[0] / xy[1]) \
    .collectAsMap()

print res

for key,val in res.items():
    print key,val


