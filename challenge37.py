import datetime
import math
from math import sqrt
import sys
import itertools
import copy
import csv
import decimal
from operator import itemgetter
from decimal import Decimal
import Eratosthenes

t = datetime.datetime.now()
tsum = 0
primes = {}

for i in Eratosthenes.get_primes((10**6)):
	primes[i] = i


for i in primes:
	if i > 10:
		truncatablePrime = True
		a = i
		for j in range(1, len(str(i))):
			a = int(a/10)
			if not(a in primes):
				truncatablePrime = False
				break
		a = i
		if truncatablePrime == True:
			for j in range(1, len(str(i))):
				b = a%(int(a/10**(int(math.log10(a))))*10**int(math.log10(a)))
				if not(b in primes):
					truncatablePrime = False
					break
				a = b
		if truncatablePrime == True:
		 	print (i)
		 	tsum +=i


print (tsum)


runtime  = datetime.datetime.now() - t
print (runtime)


