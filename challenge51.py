#0,1 = 0,2 = 0,3, 1,2 = 34 oplossingen * 100 = 3400
#
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
teller = 0
primes = {}
for i in Eratosthenes.get_primes((10**6)):
	primes[i] = i
maxPrimes = 0
candidates =[]
for i in primes:
	k = str(i)
	for j in set(str(i)):
		primesVariation = 0
		for l in range(10):
			candidate = (k.replace(j, 'x'))
			if candidate[-1] != 'x':
				candidates.append(candidate)
minPrime = 10**6
for j in set(candidates):
	primesVariation = 0
	p = []
	for k in range(10):
		l = int(j.replace('x', str(k)))
		if l in primes:
			p.append(l)
			#print (j, l, primesVariation, maxPrimes)
			if len(p) == 8 and min(p) < minPrime:
				maxPrimes = primesVariation
				minPrime = min(p)
				print (j, l, min(p))
				break

print (maxPrimes)
runtime = datetime.datetime.now() - t
print(runtime)

