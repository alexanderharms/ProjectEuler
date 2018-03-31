#-*-coding:utf8;-*-
#qpy:2
#qpy:console

#print "This is console module"
print('Calculate the sum of the digits of 100!')
from math import factorial
factorial = factorial(100)
factorialString = str(factorial)
factorialSum = 0
for ch in factorialString:
    factorialSum += int(ch)
print('Answer:')
print(factorialSum)
    
