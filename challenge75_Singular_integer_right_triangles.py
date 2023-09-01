import datetime
import math
import sys
import itertools
import euler
import Eratosthenes
#import copy
#import pandas as pd

time = datetime.datetime.now()

  
# Function to generate pythagorean  
# triplets smaller than limit 
triplets = []
def pythagoreanTriplets(limits) : 
    c, m, L, teller = 0, 2, 0,0
    # Limiting c would limit  
    # all a, b and c 
    while L < limits : 
        # Now loop on n from 1 to m-1 
        for n in range(1, m) : 
            a = m**2- n**2 
            b = 2 * m * n 
            if a>b:
                b,a = a,b
            c = m**2 + n**2 
            L = a+b+c
            # if c is greater than 
            # limit then break it 
            if L >= limits : 
                break
            if math.gcd(a,b)==1:
                triplets.append([a,b,c,L])
                teller +=1
        m = m + 1
    return teller

limit = 6*10**6
(pythagoreanTriplets(limit))
triplets2 = []
triplets3 = []
for i in triplets:
    k = 1
    while k*i[3] < limit:
        triplets2.append([i[0]*k,i[1]*k, i[2]*k, i[3]*k])
        triplets3.append(i[3]*k)
        k+=1

triplets3.sort()
counter = 0
if triplets3[0]!=triplets3[1]:
    counter +=1
if triplets3[len(triplets3)-2]!=triplets3[len(triplets3)-1]:
    counter +=1
for i in range(1, len(triplets3)-1):
    if triplets3[i-1]!=triplets3[i] and triplets3[i]!=triplets3[i+1]:
        counter +=1
    if triplets3[i]>=15*10**5:
        break
#print (len(triplets3))
print (counter)

#triplets2.sort(key=lambda x:x[3])
#for i in triplets2:
#    if i[3]<=1000:
#        print(i)

runtime  = datetime.datetime.now() - time
print (runtime)

###