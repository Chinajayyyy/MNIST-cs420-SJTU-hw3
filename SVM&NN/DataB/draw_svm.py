# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 00:34:32 2019

@author: sjtujay
"""

import numpy as np
import matplotlib.pyplot as plt

x = [10000,15000,20000,25000,30000,35000,40000,45000,50000,55000]
x = np.array(x)

#rbf accuracy
y1 = [0.9255,0.9285,0.9370,0.9400,0.9450,0.9460,0.9485,0.9495,0.9530,0.9565]
y1 = np.array(y1)
#rbf time
y2 = [46,80,123,173,233,289,356,444,507,603]
y2 = np.array(y2)

#poly accuracy
y3 = [0.8255,0.8665,0.8885,0.9040,0.9105,0.9230,0.9265,0.9345,0.9365,0.9370]
y3 = np.array(y3)
#poly time
y4 = [101,193,297,413,549,700,846,1036,1184,1375]
y4 = np.array(y4)

'''
#photo 1
plt.plot(x,y1,'r-s',label='kernel:RBF')
plt.plot(x,y3,'b-s',label='kernel:POLY')
plt.legend(loc="lower right")
plt.xlabel("Sample_size")
plt.ylabel("Accuracy")
plt.savefig('E:\\photos\\size_accuracy',dpi=1000)
plt.show()

#photo 2
plt.plot(x,y2,'r-s',label='kernel:RBF')
plt.plot(x,y4,'b-s',label='kernel:POLY')
plt.legend(loc="lower right")
plt.xlabel("Sample_size")
plt.ylabel("Run_time/s")
plt.savefig('E:\\photos\\size_time',dpi=1000)
plt.show()

'''
#photo 3
x_ = x[1:10]
y_ = []
_y = []
for i in range(9):
    y_.append(y1[i+1] - y1[i])
    _y.append(y3[i+1] - y3[i])
    
'''
plt.plot(x_,y_,'r-s',label='kernel:RBF')
plt.plot(x_,_y,'b-s',label='kernel:POLY')
plt.legend(loc="lower right")
plt.xlabel("Sample_size")
plt.ylabel("Accuracy_increasing")
plt.savefig('E:\\photos\\size_increasing',dpi=1000)
plt.show()
'''

#photo 4
tmp = []
_tmp = []
dlt = []
_dlt = []

for i in range(9):
    tmp.append(y2[i+1] - y2[i])
    _tmp.append(y4[i+1] - y4[i])

for i in range(9):
    dlt.append(y_[i] / tmp[i])
    _dlt.append(_y[i] / _tmp[i])

'''
plt.plot(x_,dlt,'r-s',label='kernel:RBF')
plt.plot(x_,_dlt,'b-s',label='kernel:POLY')
plt.legend(loc="lower right")
plt.xlabel("Sample_size")
plt.ylabel("Accuracy_increasing_per_second")
plt.savefig('E:\\photos\\size_increasing_per_second',dpi=1000)
plt.show()
'''



