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
primes = {}

for i in Eratosthenes.get_primes(4*(10**6)):
	primes[i] = i
maxN = 0

for a in range(-1000,1000):
	for b in range(-1000,1000):
		n = 0
		prime = True
		while prime == True:
			candidate = n**2+a*n+b
			if not(candidate in primes):
				prime = False
				if n >= maxN:
					maxN = n
					maxA = a
					maxB = b
					print('canidate:{:6} prime:{:1}   a:{:3} b:{:3} n:{:3}'.format(candidate, prime,a,b,n))
			n +=1

print ('Max N is {}, a*b = {}'.format(maxN,maxA*maxB))
runtime  = datetime.datetime.now() - t
print (runtime)


