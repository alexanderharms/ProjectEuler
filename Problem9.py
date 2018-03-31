# Prolem 9
# A Pythogorean triplet is a set of three natural numbers a<b<c, for which
# a^2 + b^2 = c^2
# Find the product a*b*c* for the only Pythagorean triplet for which
# a + b + c = 1000

# a = 1000 - b - c
# c = 1000 - a - b
# 1000 - b - c < b < 1000 - a - b
# 500 - 0.5*c < b < 500 - 0.5*a

# 500 - 0.5*c < b < c
# a < b < 500 - 0.5*a

# 500 - 0.5*c < c - 1
# a + 1 < 500 - 0.5*a
# 501 - 0.5*c < c
# a < 499 - 0.5*a

a = []
for i in range(1, 333):
    if i < 499 - 0.5*i:
        a.append(i)

c = []
for j in range(3, 501):
    if 501 - 0.5*j < j:
        c.append(j)

sets = []
lenA = len(a)
lenC = len(c)
print("Collecting sets")
for m in range(0, lenA):
#    print(m)
    for n in range(0, lenC):
        for k in range(a[m], c[n]):
            sumSet = a[m] + k + c[n]
            if sumSet == 1000:
                setOfThree = [a[m], k, c[n]]
                sets.append(setOfThree)
            elif sumSet > 1000:
                break
                
lenSets = len(sets)
print("Checking sets")
for p in range(0, lenSets):
#    print(p)
    trySet = sets[p]
    pythAB = trySet[0] * trySet[0] + trySet[1] * trySet[1]
    pythC = trySet[2] * trySet[2]
    if pythAB == pythC:
        answer = trySet
        break

print('Pythagoran triplet')
print(answer)
product = answer[0] * answer[1] * answer[2]
print('Product:')
print(product)

