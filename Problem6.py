# -*- coding: utf-8 -*-
"""
Created on Mon May  8 21:47:36 2017

@author: Alexander
"""

import numpy as np

numberList = np.linspace(1, 100, 100)
sumOfSquaredNumbers = sum(numberList**2)
sumOfNumbersSquared = sum(numberList)**2
difference = sumOfNumbersSquared - sumOfSquaredNumbers
print("Find the difference between the sum of squares of the first one hundred natural numbers and the square of the sum.")
print("The difference is: %i" % difference)
