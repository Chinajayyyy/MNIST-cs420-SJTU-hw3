#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 13:27:36 2019

@author: fanzhedong
"""

import numpy as np
import matplotlib.pyplot as plt
import csv

def init(a):
    for i in range(5):
        a.append([])
        for j in range(9):
            a[i].append(0)


csv_file = csv.reader(open('iris.csv','r'))
print (csv_file)
svm_linear = []
svm_rbf = []
mlp_1000 = []
mlp_2000 = []
x = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]

init(svm_linear) #0-without pca, 1-pca to 1, 2-pca to 2, 3-pca to 3, 4-pca to 4
init(svm_rbf)
init(mlp_1000)
init(mlp_2000)

cnt = 1

for line in csv_file:
    if (cnt==2 or cnt==8 or cnt==14 or cnt==20 or cnt==26):
        for i in range(9): 
            svm_linear[int(cnt/6)][i] = float(line[i+1])
        cnt+=1
        continue
    if (cnt==3 or cnt==9 or cnt==15 or cnt==21 or cnt==27):
        for i in range(9): 
            svm_rbf[int(cnt/6)][i] = float(line[i+1])
        cnt+=1
        continue
    if (cnt==4 or cnt==10 or cnt==16 or cnt==22 or cnt==28):
        for i in range(9): 
            mlp_1000[int(cnt/6)][i] = float(line[i+1])
        cnt+=1
        continue
    if (cnt==5 or cnt==11 or cnt==17 or cnt==23 or cnt==29):
        for i in range(9): 
            mlp_2000[int(cnt/6)][i] = float(line[i+1])
        cnt+=1
        continue
    cnt+=1
'''   
print(cnt)
print(svm_linear)
print(svm_rbf)
print(mlp_1000)
print(mlp_2000)
'''


plt.plot(x,svm_linear[0],color='red',marker='s',label='SVM_linear_withoutPCA')
plt.plot(x,svm_rbf[0],color='blue',marker='s',label="SVM_rbf_withoutPCA")
plt.plot(x,mlp_1000[0],color='green',marker='s',label="MLP_1000_withoutPCA")
plt.plot(x,mlp_2000[0],color='black',marker='s',label="MLP_2000_withoutPCA")
plt.legend(loc="lower left")
plt.xlabel("Testset size")
plt.ylabel("Score")
plt.savefig('/Users/fanzhedong/Desktop/all_score_withoutPCA',dpi=1000)
plt.show()



plt.plot(x,svm_linear[1],color='red',marker='s',label='SVM_linear_withPCAto1')
plt.plot(x,svm_rbf[1],color='blue',marker='s',label="SVM_rbf_withPCAto1")
plt.plot(x,mlp_1000[1],color='green',marker='s',label="MLP_1000_withPCAto1")
plt.plot(x,mlp_2000[1],color='black',marker='s',label="MLP_2000_withPCAto1")
plt.legend(loc="lower left")
plt.xlabel("Testset size")
plt.ylabel("Score")
plt.savefig('/Users/fanzhedong/Desktop/all_score_withPCAto1',dpi=1000)
plt.show()



plt.plot(x,svm_linear[2],color='red',marker='s',label='SVM_linear_withPCAto2')
plt.plot(x,svm_rbf[2],color='blue',marker='s',label="SVM_rbf_withPCAto2")
plt.plot(x,mlp_1000[2],color='green',marker='s',label="MLP_1000_withPCAto2")
plt.plot(x,mlp_2000[2],color='black',marker='s',label="MLP_2000_withPCAto2")
plt.legend(loc="lower left")
plt.xlabel("Testset size")
plt.ylabel("Score")
plt.savefig('/Users/fanzhedong/Desktop/all_score_withPCAto2',dpi=1000)
plt.show()



plt.plot(x,svm_linear[3],color='red',marker='s',label='SVM_linear_withPCAto3')
plt.plot(x,svm_rbf[3],color='blue',marker='s',label="SVM_rbf_withPCAto3")
plt.plot(x,mlp_1000[3],color='green',marker='s',label="MLP_1000_withPCAto3")
plt.plot(x,mlp_2000[3],color='black',marker='s',label="MLP_2000_withPCAto3")
plt.legend(loc="lower left")
plt.xlabel("Testset size")
plt.ylabel("Score")
plt.savefig('/Users/fanzhedong/Desktop/all_score_withPCAto3',dpi=1000)
plt.show()



plt.plot(x,svm_linear[4],color='red',marker='s',label="SVM_linear_withPCAto3")
plt.plot(x,svm_rbf[4],color='blue',marker='s',label="SVM_rbf_withPCAto3")
plt.plot(x,mlp_1000[4],color='green',marker='s',label="MLP_1000_withPCAto3")
plt.plot(x,mlp_2000[4],color='black',marker='s',label="MLP_2000_withPCAto3")
plt.legend(loc="lower left")
plt.xlabel("Testset size")
plt.ylabel("Score")
plt.savefig('/Users/fanzhedong/Desktop/all_score_withPCAto3',dpi=1000)
plt.show()



plt.plot(x,svm_linear[0],color='red',marker='s',label='SVM_linear_withoutPCA')
plt.plot(x,svm_linear[1],color='blue',marker='s',label='SVM_linear_withPCAto1')
plt.plot(x,svm_linear[2],color='green',marker='s',label='SVM_linear_withPCAto2')
plt.plot(x,svm_linear[3],color='black',marker='s',label='SVM_linear_withPCAto3')
plt.plot(x,svm_linear[4],color='orange',marker='s',label='SVM_linear_withPCAto4')
plt.legend(loc="lower left")
plt.xlabel("Testset size")
plt.ylabel("score")
plt.savefig('/Users/fanzhedong/Desktop/SVM_linear_all',dpi=1000)
plt.show()



plt.plot(x,svm_rbf[0],color='red',marker='s',label="SVM_rbf_withoutPCA")
plt.plot(x,svm_rbf[1],color='blue',marker='s',label="SVM_rbf_withPCAto1")
plt.plot(x,svm_rbf[2],color='green',marker='s',label="SVM_rbf_withPCAto2")
plt.plot(x,svm_rbf[3],color='black',marker='s',label="SVM_rbf_withPCAto3")
plt.plot(x,svm_rbf[4],color='orange',marker='s',label="SVM_rbf_withPCAto4")
plt.legend(loc="lower left")
plt.xlabel("Testset size")
plt.ylabel("score")
plt.savefig('/Users/fanzhedong/Desktop/SVM_rbf_all',dpi=1000)
plt.show()


plt.plot(x,mlp_1000[0],color='red',marker='s',label="MLP_1000_withoutPCA")
plt.plot(x,mlp_1000[1],color='blue',marker='s',label="MLP_1000_withPCAto1")
plt.plot(x,mlp_1000[2],color='green',marker='s',label="MLP_1000_withPCAto2")
plt.plot(x,mlp_1000[3],color='black',marker='s',label="MLP_1000_withPCAto3")
plt.plot(x,mlp_1000[4],color='orange',marker='s',label="MLP_1000_withPCAto4")
plt.legend(loc="lower left")
plt.xlabel("Testset size")
plt.ylabel("score")
plt.savefig('/Users/fanzhedong/Desktop/MLP_1000_all',dpi=1000)
plt.show()



plt.plot(x,mlp_2000[0],color='red',marker='s',label="MLP_2000_withoutPCA")
plt.plot(x,mlp_2000[1],color='blue',marker='s',label="MLP_2000_withPCAto1")
plt.plot(x,mlp_2000[2],color='green',marker='s',label="MLP_2000_withPCAto2")
plt.plot(x,mlp_2000[3],color='black',marker='s',label="MLP_2000_withPCAto3")
plt.plot(x,mlp_2000[4],color='orange',marker='s',label="MLP_2000_withPCAto4")
plt.legend(loc="lower left")
plt.xlabel("Testset size")
plt.ylabel("score")
plt.savefig('/Users/fanzhedong/Desktop/MLP_2000_all',dpi=1000)
plt.show()

