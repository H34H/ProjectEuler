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

def addToList(number):
	if euler.isPrime(number) == True:
		diagonalPrimes.append(number)
	diagonalNonPrimes.append(number)	
	

#primes = {}
#for i in Eratosthenes.get_primes((45*10**7)):
#	primes[i] = i
 
diagonalPrimes = [3,5,7]
diagonalNonPrimes = [1,3,5,7,9]

count = 9
for i in range(4,10**5,2):
	count += i
	addToList(count)
	count += i
	addToList(count)
	count += i 
	addToList(count)
	count += i
	addToList(count)
	if len(diagonalPrimes)/len(diagonalNonPrimes) > 0.099999999: 
		print(count, (i+1),len(diagonalPrimes), len(diagonalNonPrimes), len(diagonalPrimes)/len(diagonalNonPrimes))
	else:
		print(count, (i+1),len(diagonalPrimes), len(diagonalNonPrimes), len(diagonalPrimes)/len(diagonalNonPrimes))
		break
		
runtime = datetime.datetime.now() - t
print(runtime)

