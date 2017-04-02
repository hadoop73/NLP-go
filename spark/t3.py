# coding:utf-8



from pyspark import SparkContext,SparkConf

import os
os.environ["SPARK_HOME"] = "/home/hadoop/spark-2.0.1-bin-hadoop2.7"   #KeyError: 'SPARK_HOME'
conf = SparkConf()
sc=SparkContext(appName='t3',conf=conf)

data = sc.textFile('file:///home/hadoop/PycharmProjects/NLP/spark/data/3')



res = data.filter(lambda x:len(x.strip())>0)\
    .map(lambda x:int(x.strip()))\
    .sortBy(lambda x:x) \
    .zipWithIndex() \
    .map(lambda x:(x[1],x[0])) \
    .collect()


for di in res:
    print di