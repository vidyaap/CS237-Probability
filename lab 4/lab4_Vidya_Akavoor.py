# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 17:41:15 2016

@author: vid82
"""

import random as rnd
import numpy as np
from matplotlib import pyplot as plt
import math

def deterministicLoadBalancer(n):
    array = [0]*n
    for i in range(n):
        array[array.index(min(array))] += 1
    return array
    
    
def loadBalancer(n):
    array = [0]*n
    for x in range(n):
        idx = rnd.randint(0,n-1)
        array[idx] += 1
    return max(array)
    

def loadBalancer2(n, d):
    array = [0]*n
    for x in range(n):
        idx = np.random.choice(array, d, replace = False)
        array[array.index(min(idx))] += 1
    return max(array)

    
def loadBalancerPlot():
    mean_list = []
    y_coord = []
    for i in range(3, 501):
        max_list = [0]*1000
        for j in range(1000):
            max_array = loadBalancer(i)
            max_list[j] = max_array
        mean_list += [np.mean(max_list)]
        y_coord += [(3*math.log(i))/(math.log(math.log(i)))]
    plt.figure(1)
    plt.plot(range(3,501), mean_list, linewidth = 3)
    plt.draw()
    x_coord = range(3,501)
    plt.plot(x_coord, y_coord, color = 'r', linewidth = 3)
    plt.xlabel("n")
    plt.ylabel("Mean of Max")
    plt.title("Load Balancer Plot")
    plt.show()


def loadBalancerPlot2():
    mean_list = []
    y_coord = []
    for i in range(2, 11):
        max_list = [0]*1000
        for j in range(1000):
            max_array = loadBalancer2(1000, i)
            max_list[j] = max_array
        mean_list += [np.mean(max_list)]
        y_coord += [((math.log(math.log(1000)))/(math.log(i)))+2]
    plt.figure(1)
    plt.plot(range(2,11), mean_list, linewidth = 3)
    plt.draw()
    x_coord = range(2, 11)
    plt.plot(x_coord, y_coord, color = 'r', linewidth = 3)
    plt.xlabel("d")
    plt.ylabel("Mean of Max")
    plt.title("Load Balancer Plot with randomized d-choice algorithm")
    plt.show()

#below is the entire SecondMoment file including given code and code that we wrote    
    
#class SecondMomentEstimator(object):
#    counterArray = [0]
#    m = 0
#    actualDataArray = [0]
#    #Generate a random Packet
#    def packetGenerator(self):
#        return np.random.randint(math.pow(2,14)) 
#    #Generates hash functions to use
#    def generateHashFunction(self):
#        a = np.random.random_integers(0, 100000, 4)
#        return (a[0], a[1], a[2], a[3])
#    #Use this for a 4-wise independent hash
#    def hash_4i(self, key):
#        (a,b,c,d) = self.generateHashFunction()
#        val = a * math.pow(key, 3) + b * math.pow(key, 2) + c * key + d
#        ret = int(val % len(self.counterArray))
#        return ret
#    
#    def dataStream(self, numPackets):
#        for i in range(numPackets):
#            packet = self.packetGenerator()
#            self.actualDataArray[packet] += 1.0
#            hash_val = self.hash_4i(packet)
#            self.counterArray[hash_val] += 1.0       
#        
#    def actualF2(self):
#        f2 = 0
#        for x in self.actualDataArray:
#            f2 += x**2
#        return f2
#              
#   
#    def estimateF2(self):
#        est1 = 0
#        est2 = 0
#        for x in self.counterArray:
#            est1 += x**2
#            est2 += x
#        est2 = est2**2
#        est1 = est1*(self.m/(self.m - 1.0))
#        est2 = est2*(1.0/(self.m - 1.0))
#        return est1 - est2
#
#
#    def __init__(self, m):
#       self.m = m
#       self.counterArray = [0]*m
#       self.actualDataArray = [0]*(2**14)
#       
# 
#
#def F2_plot():
#    x = []
#    yf2 = []
#    yest = []
#    for m in range(50, 2501, 50):
#        f2_est = SecondMomentEstimator(m)
#        f2_est.dataStream(1000)
#        yf2 += [f2_est.actualF2()]
#        yest += [f2_est.estimateF2()]
#        x += [m]
#    plt.figure(1)
#    plt.plot(x, yf2, color = 'r', linewidth = 3)
#    plt.plot(x, yest, color = 'b', linewidth = 3)
#    plt.title("Estimate vs Actual F2")
#    plt.xlabel("m - Number of Buckets")
#    plt.ylabel("Counts")
#    plt.show()




    