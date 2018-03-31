#-*-coding:utf8;-*-
#qpy:2
#qpy:console

print("Work in progress")
#print "This is console module"
import math
import numpy as np

def collatzStep(num, even):
    if even:
        nextNum = num/2
    else:
        nextNum = 3*num + 1
    return nextNum



startNum = np.linspace(9e5, 1e6 - 1, 1e6 - 9e5)
#print(startNum)
steps = np.zeros(len(startNum))
for i in range(0, len(startNum)):
    logCheck = 0
    num = startNum[i]
   # print(num)
    while num > 1 and not logCheck:
        even = (num % 2 == 0)
        if even:
            log = math.log(num, 2)
            logCheck = (log % 1 == 0)
        if logCheck:
            steps[i] += log 
        else:
            num = collatzStep(num, even)
            steps[i] += 1
    #print(steps[i])

answer = startNum[np.argmax(steps)]
print("Starting number, under one million, producting the longest Collatz chain")
print("Answer: %d" % answer)
        
