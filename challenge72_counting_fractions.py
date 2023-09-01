import datetime
import math
import sys
import itertools
import euler
import Eratosthenes
import copy
time = datetime.datetime.now()

primes = {}
for i in Eratosthenes.get_primes((10**5)):
	primes[i] = i

f ={}

def primeFactors(number):
    for i in primes:
        if number * i < 10**5+1:
            f[number*i].append(i)
            primeFactors(number*i)
        else:
            break
    return


for i in primes:
    if i < 10**5+1:
        f[i] = [i]
        primeFactors(i)
    else:
        break

print (len(f))

def totient(number):
    if number in primes:
        return number -1
    else:
        factors = checkPrimeFactors(d)
        for p in factors:
            number *= (1-1/p)
        return int(number)

#voor priem p: rpf = p-1
#a = {}
#for d in range(2,10**6+1):
    #a = checkPrimeFactors(d)
    #print (d, totient(d))
 #   if d%10**4==0:
 #       print (d)

#print (a)
runtime  = datetime.datetime.now() - time
print (runtime)

###