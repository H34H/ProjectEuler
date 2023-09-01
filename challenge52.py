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
for i in Eratosthenes.get_primes((10**1)):
	primes[i] = i

#It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
#
#Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
candidates = {}
for i in range(10**6):
	candidates[i] = [i]

for i in range(1,10**6):
	n = []
	o = []
	for j in range(1,7):
		n.append(''.join(sorted(str(i*j))))
		o.append(i*j)
	if len(set(n)) == 1:
		print (o, set(n), len(set(n)))
		break


#print (len(candidates))
runtime = datetime.datetime.now() - t
print(runtime)

