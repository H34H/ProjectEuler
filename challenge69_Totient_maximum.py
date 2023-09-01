import datetime
import math
import sys
import itertools
import euler
import Eratosthenes
time = datetime.datetime.now()

primes = {}
maxTotient = 0
maxN = 0

for i in Eratosthenes.get_primes((10**6)):
	primes[i] = i

for i in range(510510, 10**6):
    relativePrime = 1
    if i in primes:
        relativePrime = i -1
    else:
        for j in range (2, i):
            if math.gcd(i,j) == 1:
                relativePrime += 1
                #print (i,j)
    if i/relativePrime > maxTotient:
        maxTotient = i/relativePrime
        maxN = i
        print (maxN, maxTotient, i, relativePrime)
    #if i % 10**4 == 0:
        print (i, maxN, maxTotient)
    #print (i, relativePrime, i/relativePrime, maxN, maxTotient)

print (maxN, maxTotient)

runtime  = datetime.datetime.now() - time
print (runtime)

###