# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 11:30:04 2016

@author: Vidya Akavoor
"""

import random
import numpy as np
from numpy.random import randint
from matplotlib import pyplot as plt


#original function
def dieRoll():
    y_series = randint(1,7,(1,10000))
    y_series = y_series[0]
    plt.figure(1)
    plt.hist(y_series, bins = 6, rwidth = .7, align = 'mid',\
     weights = np.zeros_like(y_series) + 1. / y_series.size)
    plt.xlim(1,6)
    plt.title("Rolling a Die")
    plt.xlabel("Value")
    plt.ylabel("Probability")
    plt.show()

#my function
def dieroll(m):
    sum_list = [0 for x in range(10000)]
    for i in range(10000):
        roll_sum = 0
        for j in range(m):
            roll = random.choice(range(1,7))
            roll_sum += roll
        sum_list[i] = roll_sum

    plt.figure(1)
    plt.hist(sum_list, bins = 6*m, rwidth = .7, align = 'mid',\
    weights = np.zeros_like(sum_list) + 1. / len(sum_list))
    plt.xlim(1,6*m)
    plt.title("Rolling a Die " + str(m) + " Time(s)")
    plt.xlabel("Value")
    plt.ylabel("Probability")
    plt.show()
    
dieroll(100)
