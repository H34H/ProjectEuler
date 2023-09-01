import datetime
import math
import sys
import itertools
import euler
import Eratosthenes
time = datetime.datetime.now()

primes = {}
for i in Eratosthenes.get_primes((10**5)):
	primes[i] = i

minPhi = 100000

subPrimes = list(filter(lambda x:x>10**3, primes))
numbersToTest = (len(subPrimes))
for i in range(0, numbersToTest):
    #print (i)
    j = i
    for j in range(i, numbersToTest):  
        number = subPrimes[i] * subPrimes[j]     
        if number < 10**7:
            phi = int(number * (1-1/subPrimes[i]) * (1-1/subPrimes[j]))
            if sorted(str(phi))==sorted(str(number)) and number/phi < minPhi:
                minPhi = number/phi
                phiPhi = phi 
                minNumber = number
                #print (number, subPrimes[i], subPrimes[j], phi, number/phi )
        else:
            #print ("door naar het volgende nummer",i, j, i*j)
            break
print (minNumber, phiPhi, minPhi)
runtime  = datetime.datetime.now() - time
print (runtime)

###