# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 13:36:49 2016

@author: vid82
"""

import random
from matplotlib import pyplot as plt
import numpy as np
import math
#import pandas as pd
from decimal import Decimal as d
import hashlib


def Bernoulli_trial(p):
    choice = random.random()
    if choice <= p:
        return 1
    else:
        return 0


def Bernoulli_hist(p, m):
    result_list = [0 for x in range(m)]
    for i in range(1000):
        result_list[i] = Bernoulli_trial(p)
    plt.figure(1)
    plt.hist(result_list, bins = 2, rwidth = .7, align = 'mid',\
    weights = np.zeros_like(result_list) + 1. / len(result_list))
    plt.xlim(0, 1)
    ax1 = plt.axes()
    ax1.set_xticks([.25, .75])
    ax1.set_xticklabels([0, 1])
    plt.title("1000 Bernoulli trials")
    plt.xlabel("True or False")
    plt.ylabel("Probability")
    plt.show()


def binomial_draw(n,p):
    count = 0
    for x in range(n):
        if Bernoulli_trial(p):
            count += 1
    return count
    

def binom_trials(n, p, numExpts):
    trial_list = [0] * numExpts
    for i in range(numExpts):
        trial_list[i] = binomial_draw(n,p)
    return trial_list


def binom_hist(n, p, numExpts):
    y_coords = binom_trials(n, p, numExpts)
    plt.figure(1)
    plt.hist(y_coords, bins = n, rwidth = .7, align = 'mid',\
    weights = np.zeros_like(y_coords) + 1. / len(y_coords))
    plt.title("1000 Binomial trials")
    plt.xlabel("Number of Successes")
    plt.ylabel("Probability")
    plt.show()

#binom_hist(1000, .4, 10000)

def nCr(n, r):
    return math.factorial(n)/math.factorial(r)/math.factorial(n-r)


def S_step_prob(steps):
    answers = []
    for L in range(steps+1):
        S = -2*L + steps
        choose = nCr(steps, L)
        for x in range(choose):
            answers += [S]
    plt.figure(1)
    plt.hist(answers, bins = steps+1, rwidth = .7, align = 'mid',\
    weights = np.zeros_like(answers) + 1. / len(answers), color = 'r')
    plt.xlim(-(steps+1), (steps+1))
    plt.title("Scarface PDF")
    plt.xlabel("Number of Steps (s)")
    plt.ylabel("Probability (Pr[S = s])")
    plt.show()
    
def J_step_prob(steps):
    answers = []
    for L in range(steps+1):
        J = -2*L + steps
        choose = nCr(steps, L)
        answers += [J]*choose
    plt.figure(1)
    plt.hist(answers, bins = steps+1, rwidth = .7, align = 'mid',\
    weights = np.zeros_like(answers) + 1. / len(answers), color = 'b')
    plt.xlim(-(steps+1), (steps+1))
    plt.title("Diamond Jim PDF")
    plt.xlabel("Number of Steps (j)")
    plt.ylabel("Probability (Pr[J = j])")
    plt.show()


def S_step_pdf(steps):
    plt.figure(6)
    xcoord = range(-steps, (steps+1))
    ycoord = [0] * ((2*steps) + 1)
    for i in range(steps):
        S = (-2*i) + steps
        prob = d((nCr(steps, i))) / d(2**steps)
        ycoord[steps+ S] = prob
    plt.plot(xcoord, ycoord, linestyle = '-', color = 'r')
    plt.xlim(-(steps+1), (steps+1))
    plt.title("Scarface PDF")
    plt.xlabel("Number of Steps (s)")
    plt.ylabel("Probability (Pr[S = s])")
    plt.show()
    return ycoord

def J_step_pdf(steps):
    plt.figure(2)
    xcoord = range(-steps, (steps+1))
    ycoord = [0] * ((2*steps) + 1)
    for i in range(steps):
        J = (-2*i) + steps
        prob = d((nCr(steps, i))) / d(2**steps)
        ycoord[steps+ J] = prob
    plt.plot(xcoord, ycoord, linestyle = '-', color = 'b')
    plt.xlim(-(steps+1), (steps+1))
    plt.title("Diamond Jim PDF")
    plt.xlabel("Number of Steps (j)")
    plt.ylabel("Probability (Pr[J = j])")
    plt.show()
    return ycoord


def prob_D(stepsS, stepsJ):
    distJ = J_step_pdf(stepsJ)
    d_prob = 0
    for i in range(stepsS+1):
        total_steps = -i + (stepsS-i)
        temp = d(distJ[stepsJ + total_steps])
        temp += d(distJ[stepsJ + total_steps+1])
        temp += d(distJ[stepsJ + total_steps+2])
        temp += d(distJ[stepsJ + total_steps-1])
        temp += d(distJ[stepsJ + total_steps-2])
        temp *= (d(nCr(stepsS, i))/d(2**stepsS))**2
        d_prob += temp
    print d_prob



def blocks_per_day():
    blocks = []
    with open('real_bitcoin.csv') as r:
        lines = [line.split('\t') for line in r]
        for x in lines:
            x =x[:-1]
            blocks += [x[1]]
    blocks = blocks[0:-6]
    blocks = map(float, blocks)
    i = 0
    while i<(len(blocks)-1):     
        blocks[i] = blocks[i+1]-blocks[i]
        i += 1
    blocks = blocks[:-1]
    coins = [(y/12.5) for y in blocks]
    #print coins
    plt.figure(3)
    plt.hist(coins, bins = 6, rwidth = .7, align = 'mid',\
    weights = np.zeros_like(coins) + 1. / len(coins), color = 'b')
    plt.title("Blocks confirmed per day")
    plt.xlabel("Number of blocks (b)")
    plt.ylabel("Probability (Pr[B = b])")
    plt.show()

##print(hashlib.sha256(b'wubba lubba dub dub').hexdigest())
#
def hash_exp(num_zeros):
    while True:
        s = random.randint(0, 99999999999)
        hash_val = hashlib.sha256(b'wubba lubba dub dub'+str(s)).hexdigest()
        hash_val2 = int(hash_val, 16)
        if hash_val2 < (2**(256-num_zeros)):
            return s, hash_val
    return s
hash_exp(15)

def fake_hash_exp(num_zeros,trials):
    v1 = [0]*trials
    for i in range(trials):
        hash_val = random.randint(0, (2**(256))-1)
        if hash_val < (2**(256-num_zeros)):
            v1[i] = 1
    return v1


def inter_arrival():
    v1 = fake_hash_exp(6, 500000)
    count = 0
    v2 = []
    for i in range(len(v1)):
        if v1[i] == 0:
            count += 1
        else:
            v2 += [count]
            count = 0
    return v2


def inter_arrival_hist():
    v2 = inter_arrival()
    plt.figure(4)
    plt.hist(v2, bins = 20, rwidth = .5, align = 'mid',\
    weights = np.zeros_like(v2) + 1. / len(v2), color = 'b')
    plt.title("Inter-arrival times")
    plt.xlabel("Times (t)")
    plt.ylabel("Probability (Pr[T = t])")
    plt.show()
 
inter_arrival_hist()

def success_count_hist():
    v1 = fake_hash_exp(6,500000)
    count = v1[0]
    v3= []
    i = 1
    while i<len(v1):
        if i%1000 == 0 and i !=0:
            count += v1[i]
            v3 += [count]
            count = 0
        else:
            count += v1[i]
        i += 1
    v3+=[count]
    plt.figure(5)
    plt.hist(v3, bins = max(v3)-min(v3), rwidth = .5, align = 'mid',\
    weights = np.zeros_like(v3) + 1. / len(v3), color = 'b')
    lamda = np.mean(v3)
    plt.title("Success Count")
    plt.xlabel("Successes (s)")
    plt.ylabel("Probability (Pr[S = s])")
    x = np.linspace(0, max(v3), len(v3))
    length = len(x)
    y = []
    for i in range(length):
        y += [((math.e**(-lamda))*(lamda**int(x[i])))/math.factorial(int(x[i]))]
    plt.plot(x, y, linestyle = '-', color = 'r', linewidth = 4)
    plt.draw()
    plt.show()

#success_count_hist()