#-*-coding:utf8;-*-
#qpy:2
#qpy:console

#print "This is console module"
print('Calculate the sum of the digits of 2**1000')

power = 2**1000
powerString = str(power)
powerSum = 0
for ch in powerString:
    powerSum += int(ch)
print('Answer:')
print(powerSum)
    
