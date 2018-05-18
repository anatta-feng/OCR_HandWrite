# -*- coding:utf-8 -*-
import numpy as np
import operator
import os


def create_data_set():
    group_vector = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels_vector = ['A', 'A', 'B', 'B']
    return group_vector, labels_vector


def img2vector(filename):
    return_vector = np.zeros((1, 1024))
    file = open(filename)
    for i in range(32):
        line = file.readline()
        for j in range(32):
            return_vector[0, 32 * i + j] = int(line[j])
    return return_vector


filename = os.path.abspath(os.path.dirname(__file__))
filename = os.path.join(filename, 'digits', 'trainingDigits', '0_0.txt')
vec = img2vector(filename)[0, 0:31]
print(vec)
