# coding:utf-8



import numpy as np
import time
import matplotlib.pyplot as plt
import random


def initCentroids(dataSet, k):
    numSamples,dim = dataSet.shape
    centroids = np.zeros((k,dim))
    for i in range(k):
        # floor(x) 小于等于x的最大整数 floor(-1.5)=-2.0
        # round(x) 四舍五入 ,round(-1.5)= -1.0
        # int(x) 只保留整数部分
        index = int(random.uniform(0,numSamples)) # random.uniform(x,y) x,y之间产生一个随机浮点数
        centroids[i,:] = dataSet[index,:]
    return centroids

# 欧几里得距离
def euclDistance(param, param1):
    #print param,param1
    return np.sqrt(np.sum(np.power(param-param1,2)))


"""
http://blog.csdn.net/zouxy09/article/details/17589329
"""
def kmeans(dataSet,k):
    numSamples = dataSet.shape[0]
    # 第一列存储数据所属的类簇,第二列存储数据与中心店的误差
    clusterAssment = np.mat(np.zeros((numSamples,2)))
    clusterChanged = True

    # 第一步,初始中心点
    centroids = initCentroids(dataSet,k)

    while clusterChanged:
        clusterChanged = False
        # 对于每一个数据
        for i in xrange(numSamples):
            minDist = 10000.0
            minIndex = 0
            # 第二步,计算数据最近的中心点
            for j in range(k):
                distance = euclDistance(centroids[j,:],dataSet[i,:])
                #print distance
                if distance < minDist:
                    minDist = distance
                    minIndex = j

            # 第三步,更新数据所属的类簇
            if clusterAssment[i,0]!=minIndex:
                clusterChanged = True
                clusterAssment[i,:]= minIndex,minDist**2   # 更新中心点和距离

        # 第四步,更新中心点
        for j in range(k):
            pointsInCluster = dataSet[np.nonzero(clusterAssment[:,0].A==j)[0]]
            centroids[j,:] = np.mean(pointsInCluster,axis=0)
    print 'Cluster completed!!'
    return centroids,clusterAssment


def showCluster(dataSet,k,centroids,clusterAssment):
    numSamples,dim = dataSet.shape
    if dim != 2:
        print "dim only 2"
        return 1

    mark = ['or','ob','og','ok','^r','+r','sr','dr','<r','pr']
    if k > len(mark):
        return 1

    for i in xrange(numSamples):
        markIndex = int(clusterAssment[i,0])
        plt.plot(dataSet[i,0],dataSet[i,1],mark[markIndex])

    mark = ['Dr','Db','Dg','Dk','^b','+b','sb','db','<b','pb']
    for i in range(k):
        plt.plot(centroids[i,0],centroids[i,1],mark[i],markersize=12)

    plt.show()


dataSet = []
import re
p = re.compile(r'\s+')
with open('testSet.txt') as f:
    for line in f.readlines():
        lineArr = p.split(line.strip())
        dataSet.append([float(lineArr[0]),float(lineArr[1])])


dataSet = np.mat(dataSet)
k = 4
centroids,clusterAssment = kmeans(dataSet,k)
showCluster(dataSet,k,centroids,clusterAssment)







