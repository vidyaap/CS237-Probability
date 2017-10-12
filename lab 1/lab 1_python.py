# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
import numpy as np
from numpy.random import randint
from matplotlib import pyplot as plt



#Question 1
plt.figure(1)
x_coord = [1,2,3,4]
y_coord = [1,2,3,4]
plt.plot(x_coord, y_coord, marker = '', linestyle = ':', color = 'r')
plt.show()

plt.figure(2)
x_coord1 = [1,2,3,4]
y_coord1 = [1,2,3,4]
plt.plot(x_coord1, y_coord1, marker = '^', linestyle = '-', color = 'b')
plt.show()


#Question 2
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


#Question 3
def draw_point():
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)
    if ((x**2) + (y**2)) <= 1.0:
        return True
    else:
        return False


def pi_Estimate(n):
    T = 0.0
    C = 0.0
    for i in range(n):
        if draw_point() == True:
            C += 1
        T += 1
    estimate = 4*(C/T)
    print(C, 'points in the circle out of', T, 'total so pi is estimated to be', estimate)
    print estimate  

pi_Estimate(100000)



#Question 4
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
