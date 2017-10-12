# -*- coding: utf-8 -*-
"""
Created on Sun Oct 02 19:16:27 2016

@author: vid82
"""

'''
Bloom Filter Class 
for Bloom Filter Lab
CS237, Sharon Goldberg
'''
from bloomFilterHash import bloomFilterHash 
from matplotlib import pyplot as plt
import numpy.random as rnd
import numpy as np

class BloomFilter(object):
    #Class Variables
    numBits = 0
    bitArray = [0]
    numHashFunctions = 0
    pairwise = False
    badInserts = []
    badLookups = []
        
    def adversarialInserts(self):
        self.personalBF = [0]*self.numBits
        self.badInserts = []
        count = 0
        for i in range (16384):
            flag = True
            val = [0] * self.numHashFunctions
            for j in range (self.numHashFunctions):
                val[j] = self.hash.pairwiseHash_i(i, j)
                if self.personalBF[val[j]] != 0:
                    flag = False
            if flag:
                self.badInserts.append(val[j])
                for j in range (self.numHashFunctions):
                    count += 1
                    self.personalBF[val[j]] = 1
        for i in range(len(self.badInserts)):
            self.insert(self.badInserts[i])
        return self.badInserts

    def adversarialLookups(self):
        self.badLookups = []
        for i in range (16384):
            if i not in self.badInserts:
                if self.lookup(i):
                    self.badLookups.append(i)
        count = 0
        for i in range (len(self.badLookups)):
            if self.lookup(self.badLookups[i]):
                count += 1
        return count * 1.0 / len(self.badLookups)
   
   '''Insert function, pass it a key and insert into bloom filter'''
   def insert(self, key):
       for x in range(self.numHashFunctions):
           hashValue = self.hash.hash_i(key,x)
           self.bitArray[hashValue] = 1
#        commented lines are used for pairwise questions (16 and 19)
#        for x in range(self.numHashFunctions):
#            if self.pairwise:
#                hashValue = self.hash.pairwiseHash_i(key,x)
#            else:
#                hashValue = self.hash.hash_i(key,x)
#            self.bitArray[hashValue] = 1
    
    '''Lookup function, pass it a key and return true or false'''
    def lookup(self, key):
        for x in range(self.numHashFunctions):
            hashValue = self.hash.hash_i(key,x)
            if self.bitArray[hashValue] == 0:
                return False
        return True
#        commented lines are used for pairwise questions (16 and 19)
#        for x in range(self.numHashFunctions):
#            if self.pairwise:
#                hashValue = self.hash.pairwiseHash_i(key,x)
#            else:
#                hashValue = self.hash.hash_i(key,x)
#            if self.bitArray[hashValue] == 0:
#                return False
#        return True
    
    def rand_inserts(self):
        self.insert(str(rnd.randint(0, 100000000)))        
    
      
    def __init__(self, numBits, numHashFunctions, pairwise):
        self.numBits = numBits
        self.bitArray = [0] * numBits
        self.hash = bloomFilterHash(numBits, numHashFunctions)
        self.numHashFunctions = numHashFunctions
        self.pairwise = pairwise


def number_12():
    # this code can be used for questions 12 and 18 if you change the
    # numHashFunctions parameter and 19 if you change the pairwise parameter
    fp_list = [0] * 1000
    rand_list = [str(rnd.randint(0,100000000)) for x in range(10000)]
    for x in range(1000):
        fp_count = 0
        # change the pairwise parameter from False to True for question 19
        bf1 = BloomFilter(4095, 10, False)
        for z in range(600):
            bf1.rand_inserts()
        for i in range(len(rand_list)):
            test = bf1.lookup(rand_list[i])
            if test:
                fp_count += 1
        fp_list[x] = fp_count/10000.0
    mean = np.mean(fp_list)
    return mean
        

def number_13():
    mean_list = [0] * 29
    for k in range(2,31):
        fp_list = [0] * 1000
        rand_list = [str(rnd.randint(0,100000000)) for x in range(10000)]
        for x in range(1000):
            fp_count = 0
            bf1 = BloomFilter(4095, k)
            for z in range(600):
                bf1.rand_inserts()
            for i in range(len(rand_list)):
                test = bf1.lookup(rand_list[i])
                if test:
                    fp_count += 1
            fp_list[x] = fp_count/10000.0
        mean = np.mean(fp_list)
        print(k, mean)
        mean_list[k-2] = mean        
    plt.figure(1)
    plt.plot(range(2,31), mean_list, linestyle = "--", color = 'b')
    plt.title("Bloom Filter with 2-30 hash functions")
    plt.xlabel("Number of Hash Functions")
    plt.ylabel("Average False Positive Probability")
    plt.draw()
    plt.show()
    
    
def number_21():
    # this is used for questions 21 and 22; see comments below
    fp_list = [0] * 1000
    rand_list = [str(rnd.randint(0,100000000)) for x in range(10000)]
    for x in range(1000):
        fp_count = 0
        bf1 = BloomFilter(4095, 10, False)
        bf1.adversarialInserts()
        for i in range(len(rand_list)):
            test = bf1.lookup(rand_list[i])
            if test:
                fp_count += 1
        # switch rand_list loop for commented line below
        #fp_count = adversarialLookups()
        fp_list[x] = fp_count/10000.0
    mean = np.mean(fp_list)
    return mean
