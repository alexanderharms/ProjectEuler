#-*-coding:utf8;-*-
#qpy:2
#qpy:console

#print "This is console module"

def checkDiv(number, divArray):
    for i in range(0, len(divArray)):
        checkMod = number % divArray[i]
        if checkMod > 0:
            return 0
    return 1
 
# 420 is evenly divisible by the numbers 1 to 7, 10, 12, 14, 15 and 20
# Any multiple of this number is also evenly divisible by these numbers
incrementNum = 420

# If a number is divisible by 18, it's evenly divisible by 9
divArray = [8,11,13,16,17,18,19]

num = incrementNum
check = 0
while not check:
    num += incrementNum
    #print("Checking %d" % num)
    check = checkDiv(num, divArray)
   
print("What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?")
print("Answer is: %d " % num)
 
    
    
