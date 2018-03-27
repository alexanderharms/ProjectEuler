# -*- coding: utf-8 -*-
"""
Created on Mon May  8 21:41:31 2017

@author: Alexander
"""

runningSum = 0
for i in range(0,1000):
    if i % 3 == 0:
        runningSum += i
    elif i % 5 == 0:
        runningSum += i

print("The sum of all multiples of 3 and 5 below 1000 is: %d" % runningSum)
        