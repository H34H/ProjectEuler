import datetime
import math
from math import sqrt
import sys
import itertools
import copy
import collections
import operator
import euler
from operator import itemgetter
from decimal import Decimal
import Eratosthenes
t = datetime.datetime.now()

primes = {}
for i in Eratosthenes.get_primes((10**6)):
	primes[i] = i

def checkPrimeFactors(number):
	if number in primes:
		return 1, [number]
	else:
		primefactors =[]
		for i in primes:
			while number%i==0 and number > 0:
				number /= i
				primefactors.append(i)
			if number==1:
				return len(set(primefactors)), primefactors

teller = 0
for i in range (1,1):
#for i in range(1, 10**6):
	p = checkPrimeFactors(i)
	if p[0]==4:
		teller += 1
		#print (teller)
		if teller == 4:
			print (i, p)
			break
	else:
		teller = 0
		#break

#print (tsum)

runtime = datetime.datetime.now() - t
print(runtime)
