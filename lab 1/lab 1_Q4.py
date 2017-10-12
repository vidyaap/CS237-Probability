# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 18:42:26 2016

@author: Vidya Akavoor
"""

import random
from matplotlib import pyplot as plt
import numpy as np

def expt(p):
    count = 0
    while True:
        choice = random.random()
        if choice > p:
            count+=1
        else:
            count+=1
            break
    return count
    

def Coin_flip_test(n,p):
    count_list = []
    for x in range(n):
        count_list += [expt(p)]
    return count_list
    

def plot_cft_pmf(n,p):
    count_list = Coin_flip_test(n,p)
    plt.figure(1)
    plt.hist(count_list, bins = max(count_list), rwidth = .7, align = 'mid',\
     weights = np.zeros_like(count_list) + 1. / len(count_list))
    plt.xlim(1,max(count_list))
    plt.title("Flipping a p-biased coin with p = " + str(p) + " Probability")
    plt.xlabel("Number of Flips")
    plt.ylabel("Probability") 
    x = np.linspace(0, max(count_list), 10000)
    y = p*((1-p)**(x-1))
    plt.plot(x, y, linestyle = '-', color = 'r', linewidth = 4)
    plt.show()


plot_cft_pmf(10000, .8)

