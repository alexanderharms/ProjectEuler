# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#palindrome = 33
#palindromeStr = str(palindrome)
#print(palindromeStr[::-1])


def checkPalindrome(numberString):
    revNumberString = numberString[::-1]
    if numberString == revNumberString:
        return 1
    else:
        return 0
    
palindromes = []
for i in range(0,1000):
    for j in range(0,1000):
        product = i * j
        if checkPalindrome(str(product)):
            palindromes.append(product)
        
maxPalindrome = max(palindromes)

print("Find the largest palindrome made from the product of two 3-digit numbers")
print("Answer: %d") % (maxPalindrome)
