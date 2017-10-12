# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 18:14:26 2016

@author: Vidya Akavoor
"""

import random

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


#You need 100,000 points to consistently get the result 3.14
