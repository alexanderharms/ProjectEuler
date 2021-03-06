# -*- coding: utf-8 -*-
"""
Created on Mon May  8 21:53:08 2017

@author: Alexander
"""
import numpy as np

# Generate primes according to Wilson's theom

def primes_sieve(limit):
    limitn = int(limit+1)
    not_prime = np.zeros(limitn)
    primes = []
    for i in range(2, limitn):
        if not_prime[i]:
            continue
        for f in range(i*2, limitn, i):
            not_prime[f] = 1
                     
        primes.append(i)
    return primes

primes = primes_sieve(2e6)
sumPrimes = sum(primes)
print('The sum of primes below two million:')
print(sumPrimes)
