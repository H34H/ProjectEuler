import datetime
import math
import sys
import itertools

time = datetime.datetime.now()

pentagonalNumber = []
dictPentagonal = {}

def pentagonal(n):
    return (n * (3 * n - 1)) // 2  # the nth pentagonal number is given by (3n^2 - n)/2

def generalised_pentagonal(n):  # 0, -1, 1, -2, 2
    if n % 2 == 0:
        return pentagonal((n // 2) + 1)  # pentagonal(n/2 + 1) if n is even
    else:
        return pentagonal(-(n // 2) - 1)  # pentagonal(-(n/2 + 1)) if n is odd

for n in range(0,10**6):
	pentagonalNumber.append(generalised_pentagonal(n))
	#dictPentagonal[int(n*(3*n-1)/2)]=int(n*(3*n-1)/2)

print(pentagonalNumber[0:20])

p = []
p.append(1)
p.append(1)


n = 2
while p[n-1] % 10**6 != 0:
    part = 0
    gtZero = True
    i = 0
    j = 1
    while gtZero:
        if n-pentagonalNumber[i]>=0:
            if i%2 == 0 and i>0:
                j *= -1
            part += j*p[n-pentagonalNumber[i]]
            #print(n,i,j, n-pentagonalNumber[i],p[n-pentagonalNumber[i]])
            i+=1
        else:
            gtZero = False
            p.append(part)
    #print(n, part)
    n += 1
print(n-1)
print(part)
j = -1


runtime  = datetime.datetime.now() - time
print (runtime)

###