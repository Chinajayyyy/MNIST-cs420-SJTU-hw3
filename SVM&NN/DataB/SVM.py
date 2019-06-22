#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 16:38:54 2019

@author: fanzhedong
"""

import input_data
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import os
import random
from sklearn.svm import SVC
from sklearn import preprocessing
import time

def pred_label(label):
    for i in range(10):
        if(label[i] == 1):
            return i


mnist = input_data.read_data_sets("MNIST_data",one_hot=True)

train_image = mnist.train.images
train_label = mnist.train.labels
test_image = mnist.test.images
test_label = mnist.test.labels

#print (test_label.shape)

X=preprocessing.StandardScaler().fit_transform(train_image)
train_X = X[0:55000]
train_labels = train_label[0:55000]

train_trans_label = []
for i in range(55000):
    tmp = pred_label(train_labels[i])
    train_trans_label.append(tmp)

train_trans_label = np.array(train_trans_label)
#print (train_trans_label.shape)

np.array(train_X)
np.array(train_labels)

#print (train_X.shape)
#print (train_labels.shape)

print("Start time(sample_size:55000):")
print(time.strftime('%Y-%m-%d %H:%M:%S'))

clf = SVC(kernel="rbf")
clf.fit(train_X,train_trans_label)

x=preprocessing.StandardScaler().fit_transform(test_image)
test_x = x[0:2000]
test_labels = test_label[0:2000]

test_trans_label = []

for i in range(2000):
    tmp = pred_label(test_labels[i])
    test_trans_label.append(tmp)

test_trans_label = np.array(test_trans_label)

np.array(test_x)
np.array(test_labels)
print("Accuracy:")
print(clf.score(test_x,test_trans_label))

print("End time(sample_size:55000):")
print(time.strftime('%Y-%m-%d %H:%M:%S'))


"""
print (pred_label(train_label[3]))
print (pred_label(train_label[6]))
photo_1 = train_image[3]
photo_1 = photo_1.reshape(28,28)
photo_2 = train_image[6]
photo_2 = photo_2.reshape(28,28)

fig = plt.figure(figsize=(10,10))
ax0 = fig.add_subplot(221)
ax0.imshow(photo_1)
ax1 = fig.add_subplot(222)
ax1.imshow(photo_2)
"""


