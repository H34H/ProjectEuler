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
import euler
t = datetime.datetime.now()
tsum = 0

primes = {}
primesl = []
for i in Eratosthenes.get_primes((10**6)):
	primes[i] = i
	primesl.append(i)

start = 0
stop = 1
primeSum = 0
maxprimeSum = 0
maxRange = 0
while primeSum < 10**6:
	primeSum = sum(primesl[start:stop])
	if stop-start > maxRange and primeSum in primes:
		maxprimeSum = primeSum
		maxRange = stop-start
		print (primesl[start],primesl[stop], primeSum, maxprimeSum, maxRange)
	if primeSum < 10**6:
		if sum(primesl[start:stop+1]) < 10**6 and stop < len(primesl):
			stop +=1
		elif start < stop:
			start +=1
		elif start == stop:
			print (start,stop)
			print ('finished!')
			break
	else:
		start += 1
		stop -= 1
print (maxprimeSum)
#def checkprimesum(toBePrimed):
#	primeSum = 0
#	for j in primes:
#		primeSum += j
#		if primeSum == toBePrimed:
#			return j
#		elif primeSum > toBePrimed:
#			return 0 

#
#for toBePrimed in primes:
#	a = checkprimesum(toBePrimed)
#	if a > 0:
#		print (toBePrimed, checkprimesum(toBePrimed))

runtime = datetime.datetime.now() - t
print(runtime)
