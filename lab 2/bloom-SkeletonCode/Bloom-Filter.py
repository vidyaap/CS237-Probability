'''
Bloom Filter Class 
for Bloom Filter Lab
CS237, Sharon Goldberg
'''
from bloomFilterHash import bloomFilterHash 
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
            if self.pairwise:
                hashValue = self.hash.pairwiseHash_i(key,x)
            else:
                hashValue = self.hash.hash_i(key,x)
            self.bitArray[hashValue] = 1
    
    '''Lookup function, pass it a key and return true or false'''
    def lookup(self, key):
        for x in range(self.numHashFunctions):
            if self.pairwise:
                hashValue = self.hash.pairwiseHash_i(key,x)
            else:
                hashValue = self.hash.hash_i(key,x)
            if self.bitArray[hashValue] == 0:
                return False
        return True
    
    def rand_inserts(self):
        self.insert(str(rnd.randint(0, 100000000)))        
    
      
    def __init__(self, numBits, numHashFunctions, pairwise):
        self.numBits = numBits
        self.bitArray = [0] * numBits
        self.hash = bloomFilterHash(numBits, numHashFunctions)
        self.numHashFunctions = numHashFunctions
        self.pairwise = pairwise


fp_list = [0] * 1000
for x in range(1000):
    fp_count = 0
    bf1 = BloomFilter(4095, 6, True)
    #for z in range(600):
    bf1.adversarialInserts()
    fp_count = bf1.adversarialLookups()
#    for y in range(10000):
#        rand_key = str(rnd.randint(0,100000000))
#        test = bf1.lookup(rand_key)
#        if test:
#            fp_count += 1
    fp_list[x] = fp_count
mean = np.mean(fp_list)
maximum = np.max(fp_list)
print(mean, maximum)