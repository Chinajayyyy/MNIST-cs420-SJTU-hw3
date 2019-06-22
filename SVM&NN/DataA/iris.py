# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 20:04:06 2019

@author: sjtujay
"""

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.neural_network import MLPClassifier
from sklearn.decomposition import PCA

#import data. X is data and y is labels
iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target
#print (iris_X.shape)
#print (iris_y.shape)

score = score_rbf = score_mlp = score_mlp_2 = 0
score_pca = score_rbf_pca = score_mlp_pca = score_mlp_2_pca = 0

for i in range(10):
    
#split X, xx% for train and xx% for test
    X_train,X_test,y_train,y_test=train_test_split(iris_X,iris_y,test_size=0.9)
#print (y_test.shape)

#using pca on data
    pca = PCA(n_components=4)
    pca_X_train = pca.fit_transform(X_train)
    pca_X_test = pca.fit_transform(X_test)
#print (pca_X_train.shape)

#without pca
#train model without pca
    svc = svm.SVC(kernel="linear").fit(X_train,y_train)
    svc_rbf = svm.SVC(kernel="rbf").fit(X_train,y_train)
    mlp = MLPClassifier(max_iter=1000).fit(X_train,y_train)
    mlp_2 = MLPClassifier(max_iter=2000).fit(X_train,y_train)

#test model
    score += svc.score(X_test,y_test)
    score_rbf += svc_rbf.score(X_test,y_test)
    score_mlp += mlp.score(X_test,y_test)
    score_mlp_2 += mlp_2.score(X_test,y_test)
    
#with pca
    svc_pca = svm.SVC(kernel="linear").fit(pca_X_train,y_train)
    svc_rbf_pca = svm.SVC(kernel="rbf").fit(pca_X_train,y_train)
    mlp_pca = MLPClassifier(max_iter=1000).fit(pca_X_train,y_train)
    mlp_2_pca = MLPClassifier(max_iter=2000).fit(pca_X_train,y_train)
    
#test model
    score_pca += svc_pca.score(pca_X_test,y_test)
    score_rbf_pca += svc_rbf_pca.score(pca_X_test,y_test)
    score_mlp_pca += mlp_pca.score(pca_X_test,y_test)
    score_mlp_2_pca += mlp_2_pca.score(pca_X_test,y_test)
'''
print("svc_linear:" + str(score))
print("svc_rbf:" + str(score_rbf))
print("mlp:" + str(score_mlp))
print("mlp_2:" + str(score_mlp_2))
'''






print("svc_linear:" + str(score/10))
print("svc_rbf:" + str(score_rbf/10))
print("mlp:" + str(score_mlp/10))
print("mlp_2:" + str(score_mlp_2/10))
print("svc_linear_pca:" + str(score_pca/10))
print("svc_rbf_pca:" + str(score_rbf_pca/10))
print("mlp_pca:" + str(score_mlp_pca/10))
print("mlp_2_pca:" + str(score_mlp_2_pca/10))

