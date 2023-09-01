import datetime
import math
import sys
import itertools
import euler
import Eratosthenes
time = datetime.datetime.now()

primes = {}
for i in Eratosthenes.get_primes((10**6)):
	primes[i] = i

n7 = 3
d7 = 7
minDistance = 10
n = n7
d = d7

for d in range(999*10**3,10**6):
    n = int((n7 / d7) * d)
    if n/d-n7/d7 < minDistance and math.gcd(n,d)==1:
        minDistance = n7/d7-n/d
        minN = n
        minD = d
        print (n, d, n/d-3/7)

runtime  = datetime.datetime.now() - time
print (runtime)

###