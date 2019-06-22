# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 13:19:34 2019

@author: sjtujay
"""

import numpy as np
import matplotlib.pyplot as plt

x = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,11000,12000,13000,14000,15000,16000,17000,18000,19000,20000]
x = np.array(x)
y1 = [0.9615,0.9737,0.9810,0.9840,0.9884,0.9872,0.9894,0.9904,0.9900,0.9909,0.9908,0.9907,0.9908,0.9922,0.9912,0.9907,0.9910,0.9927,0.9920,0.9918]
y1 = np.array(y1)
y2 = [85,167,246,326,415,482,564,644,728,861,862,952,1076,1177,1309,1431,1456,1529,1623,1611]
y2 = np.array(y2)

'''
#photo 1
plt.plot(x,y1,'r-s',label='CNN')
plt.legend(loc="lower right")
plt.xlabel("Iteration_times")
plt.ylabel("Accuracy")
plt.savefig('E:\\photos\\iteration_accuracy',dpi=1000)
plt.show()
'''
'''
#photo 2
plt.plot(x,y2,'r-s',label='CNN')
plt.legend(loc="lower right")
plt.xlabel("Iteration_times")
plt.ylabel("Run_time/s")
plt.savefig('E:\\photos\\iteration_time',dpi=1000)
plt.show()
'''

#photo 3
x_ = x[1:20]
tmp = []
for i in range(19):
    tmp.append(y1[i+1] - y1[i])
tmp = np.array(tmp)
'''
plt.plot(x_,tmp,'r-s',label='CNN')
plt.legend(loc="lower right")
plt.xlabel("Iteration_times")
plt.ylabel("Accuracy increasing rate")
plt.savefig('E:\\photos\\iteration_accuracy_rate',dpi=1000)
plt.show()
'''

#photo 4
tmp2 = []
_tmp2 = []
for i in range(19):
    tmp2.append(y2[i+1] - y2[i])
for i in range(19):
    _tmp2.append(tmp[i] / tmp2[i])

_tmp2 = np.array(_tmp2)
'''
plt.plot(x_,_tmp2,'r-s',label='CNN')
plt.legend(loc="lower right")
plt.xlabel("Iteration_times")
plt.ylabel("Accuracy increasing rate per second")
plt.savefig('E:\\photos\\iteration_accuracy_rate_per_second',dpi=1000)
plt.show()
'''
