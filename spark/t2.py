# coding:utf-8



from pyspark import SparkContext,SparkConf
from pyspark.sql import SQLContext
from pyspark.sql.types import *

import os
os.environ["SPARK_HOME"] = "/home/hadoop/spark-2.0.1-bin-hadoop2.7"   #KeyError: 'SPARK_HOME'
conf = SparkConf()
sc=SparkContext(appName='t2',conf=conf)

two = sc.textFile('file:///home/hadoop/PycharmProjects/NLP/spark/data/2')
d = two.map(lambda x:str(x)).filter(lambda x:str(x) if len(str(x).strip())>0 else "").map(lambda x:(str(x).strip(),""))\
    .groupByKey().sortByKey().keys().collect()

for di in d:
    print di





