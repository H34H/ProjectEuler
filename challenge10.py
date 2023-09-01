import datetime
import math
import sys
import itertools
t = datetime.datetime.now()

n = 3
IsPrime = False
primes = []

max = 2000000

#for i in range (1,2000000,6):
#	primes.append(i-1)
#	primes.append(i+1)

def primes_sieve2(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

for p in primes_sieve2(max):
	primes.append(p)
print (len(primes))
s = sum(primes)
print (s)
#print (primes)
runtime  = datetime.datetime.now() - t
print (runtime)

###