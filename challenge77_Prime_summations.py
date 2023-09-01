import datetime
import math
import sys
import itertools
import euler
import Eratosthenes
import copy

time = datetime.datetime.now()
getal = 10
teller = 0

primes = []
for i in Eratosthenes.get_primes((10**4)):
	primes.append(i)

def summation(goalNumber, pastNumber, remainder):
    global teller
    if remainder == 0:
        teller += 1
        #print("=", teller)
    else:
        i = 0
        while primes[i] < min(pastNumber,remainder)+1 and i < len(primes):
            #print (i, remainder)
            summation(goalNumber, primes[i], remainder-primes[i])
            if i < len(primes)-1:
                i +=1
            else:
                break
getal = 0
while teller < 5000:
    teller = 0
    summation(getal,getal-1,getal)
    print (getal, teller)
    getal +=1
runtime  = datetime.datetime.now() - time
print (runtime)

###