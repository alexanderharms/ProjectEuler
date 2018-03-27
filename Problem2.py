#-*-coding:utf8;-*-
#qpy:2
#qpy:console

#print "This is console module"
first = 1
second = 2
fib = first + second
first = second
second = fib
fibSum = 2
while fib < 4e6:
    fib = first + second
    if fib % 2 == 0:
        fibSum += fib
    first = second
    second = fib
print("Find the sum of the even-valued terms out of the Fibonacci sequence, not exceeding four million.")
print("Answer: %d" % fibSum)
