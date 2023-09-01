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

primes = []
for i in Eratosthenes.get_primes((10**5)):
	primes.append(i)

odds = []
for i in range(1,10**5,2):
	odds.append(i)

candidates = (set(odds)-set(primes))

numbers = []
for i in primes:
	for j in range(0, int(math.sqrt(10**5))):
		numbers.append(i+2*j**2)

print ((candidates-set(numbers)))

#print (tsum)

runtime = datetime.datetime.now() - t
print(runtime)
