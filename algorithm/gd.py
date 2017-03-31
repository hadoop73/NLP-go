# coding:utf-8

import random
import numpy as np

# 自变量的输入值可能超出定义域的范围
def safe(f):
    def safe_f(*args,**kwargs):
        try:
            return f(*args,**kwargs)
        except:
            return float('inf')
    return safe_f


def step(theta, gradient, step_size):
    return [v_i + step_size*gradient for v_i,gradient in zip(theta,gradient)]


def minimize_batch(target_fn,gradient_fn,theta_0,tolerance=0.00001,maxIter=100):
    step_sizes = [100,10,1,0.1,0.001,0.001]
    theta = theta_0
    target_fn = safe(target_fn)
    value = target_fn(theta)
    t = 1
    while True:
        gradient = gradient_fn(theta)
        print gradient
        next_thetas = [step(theta,gradient,-step_size)
                       for step_size in step_sizes ]

        # 选择最小的点
        next_theta = min(next_thetas,key = target_fn)
        next_value = target_fn(next_theta)
        t += 1
        if t>=maxIter:
            return theta, value,t
        # 停止准则
        if abs((value-next_value)/value) < tolerance:
            return theta,value,t
        else:
            theta,value = next_theta,next_value


max_iter = 5
iter = 1
theta_0 = [random.randint(-10,10)*1.0 for i in range(3)]
print theta_0

# 向量平方和
def sum_of_squares(v):
    return np.dot(v,v)

# 定义梯度
def sum_of_squares_gradient(v):
    return [2*v_i for v_i in v]


theta,value,iter = minimize_batch(target_fn=sum_of_squares,gradient_fn=sum_of_squares_gradient,
                                 theta_0=theta_0)



print "最后结果:", theta,value,iter






