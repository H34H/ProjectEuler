import datetime
import os
from math import inf, lcm, log10, sqrt
import Eratosthenes

time = datetime.datetime.now() 

primes = set()
for i in Eratosthenes.get_primes(int(sqrt(50*10**6))):
	primes.add(i)

primes = sorted(primes)

primePowerTriples = set()
for a in primes:
    if a**4 >= 50 * 10**6:
	    break
    else:
        for b in primes:
            if a**4 + b**3 >= 50 * 10**6:
                break
            else:
                for c in primes:
                    if a**4 + b**3 + c**2 < 50*10**6:
                        primePowerTriples.add(a**4 + b**3 + c**2)
                    else:
                        break	
print (len(primePowerTriples))
runtime  = datetime.datetime.now() - time
print (runtime)
