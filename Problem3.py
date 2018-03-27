#-*-coding:utf8;-*-

import numpy as np
number = 600851475143
#number = 13195
#number = 15

# Find the largest prime factor

# This is an odd number
# An odd number can only be factorized
# into odd numbers

def primes_sieve(limit):
    limitn = int(np.ceil(np.sqrt(limit+1)))
    not_prime = np.zeros(limitn)
    primes = []
    for i in range(2, limitn):
        if not_prime[i]:
            continue
        for f in range(i*2, limitn, i):
            not_prime[f] = 1
                     
        primes.append(i)
    return primes

primelist = primes_sieve(number)
divisiblePrimes = []
for i in reversed(range(len(primelist))):
    modulo = number % primelist[i]
    if modulo == 0:
        divisiblePrimes.append(primelist[i])
    
#print(divisiblePrimes)
print("Largest divisible prime under %d is %d") % (number, max(divisiblePrimes))
#printNum = np.prod(divisiblePrimes, dtype='float64')
#print(printNum)
    
