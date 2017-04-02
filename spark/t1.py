# coding:utf-8



from pyspark import SparkContext,SparkConf
from pyspark.sql import SQLContext
from pyspark.sql.types import *

import os
os.environ["SPARK_HOME"] = "/home/hadoop/spark-2.0.1-bin-hadoop2.7"   #KeyError: 'SPARK_HOME'
conf = SparkConf()
sc=SparkContext(appName='t1',conf=conf)

"""
0067011990999991950051507004888888889999999N9+00001+9999999999999999999999

数据说明：
第15-19个字符是year
第45-50位是温度表示，+表示零上 -表示零下，且温度的值不能是9999，9999表示异常数据
第50位值只能是0、1、4、5、9几个数字
"""

data = sc.textFile('file:///home/hadoop/PycharmProjects/NLP/spark/data/1')

def f(line):
    year = int(line[15:19])
    temper = int(line[46:50])
    if line[45]=="-":
        temper *= -1
    if line[50] in "01459" and temper != 9999:
        return (year,temper)

def prnt(x):
    print "year:", x[0], "max: ", x[1]
res = data.map(f).reduceByKey(lambda x,y:max(x,y)).sortByKey().collect()

print type(res)

for x in res:
    prnt(x)















