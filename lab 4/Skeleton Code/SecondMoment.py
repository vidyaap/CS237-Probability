'''
CS237 Lab 5
Sharon Goldberg
'''
import numpy as np
import math
from matplotlib import pyplot as plt

class SecondMomentEstimator(object):
    counterArray = [0]
    m = 0
    actualDataArray = [0]
    #Generate a random Packet
    def packetGenerator(self):
        return np.random.randint(math.pow(2,14)) 
    #Generates hash functions to use
    def generateHashFunction(self):
        a = np.random.random_integers(0, 100000, 4)
        return (a[0], a[1], a[2], a[3])
    #Use this for a 4-wise independent hash
    def hash_4i(self, key):
        (a,b,c,d) = self.generateHashFunction()
        val = a * math.pow(key, 3) + b * math.pow(key, 2) + c * key + d
        ret = int(val % len(self.counterArray))
        return ret
    
    def dataStream(self, numPackets):
        for i in range(numPackets):
            packet = self.packetGenerator()
            self.actualDataArray[packet] += 1.0
            hash_val = self.hash_4i(packet)
            self.counterArray[hash_val] += 1.0       
        
    def actualF2(self):
        f2 = 0
        for x in self.actualDataArray:
            f2 += x**2
        return f2
              
   
    def estimateF2(self):
        est1 = 0
        est2 = 0
        for x in self.counterArray:
            est1 += x**2
            est2 += x
        est2 = est2**2
        est1 = est1*(self.m/(self.m - 1.0))
        est2 = est2*(1.0/(self.m - 1.0))
        print est1 - est2
        return est1 - est2


    def __init__(self, m):
       self.m = m
       self.counterArray = [0]*m
       self.actualDataArray = [0]*(2**14)
       
 

def F2_plot():
    x = []
    yf2 = []
    yest = []
    for m in range(50, 2501, 50):
        f2_est = SecondMomentEstimator(m)
        f2_est.dataStream(1000)
        yf2 += [f2_est.actualF2()]
        yest += [f2_est.estimateF2()]
        x += [m]
    plt.figure(1)
    plt.plot(x, yf2, color = 'r', linewidth = 3)
    plt.plot(x, yest, color = 'b', linewidth = 3)
    plt.title("Estimate vs Actual F2")
    plt.xlabel("m - Number of Buckets")
    plt.ylabel("Counts")
    plt.show()


F2_plot()


