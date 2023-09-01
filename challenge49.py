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

primes = []
for i in Eratosthenes.get_primes((10**5)):
	primes.append(i)

numbers = [1,2,3,4,5,6,7,8,9,0]
for i in itertools.permutations(numbers,4):
	numbers.append(i[0]*10**3+i[1]*10**2+i[2]*10+i[3])

def calcPermutations(numbers):
	result = {}
	numbers = str(numbers)
	for i in itertools.permutations(numbers):
		d = (int(''.join(i)))
		result[d] = d
	return result

#print (calcPermutations(9990))

i = 0
while primes[i] < 10000:
	for j in itertools.permutations(str(primes[i])):
		d = (int(''.join(j)))
		td = d+(d-primes[i])
		if td>1000 and d in primes and td in primes and td in calcPermutations(d*10) and d != td and len(str(primes[i])+str(d)+str(td))==12 and d > primes[i] and td>d:
			print (primes[i],d, td)

	i +=1


#sortedCandidates = []
#for i in candidates:
#	teller = []
#	for j in itertools.permutations(str(i),4):
#		k = int(''.join(j))
#		if k in primes: # and k-teller[-1]==3330:
#			teller.append(k)
#	if len(teller) >= 3:
#		teller.sort()
#		sortedCandidates.append(teller)

#sortedCandidates.sort(key=itemgetter(0))
#print (len(sortedCandidates))
#for i in sortedCandidates:
	#print (i)
#	for j in range(0, len(i)):
#		for k in range(j+1, len(i)):
#			for l in range(k+1, len(i)):
#				if (i[l]-i[k] == i[k]-i[j]):
				#if i[j] == 1487:
#					print(i[j],i[k],i[l])
#print (((sortedCandidates)))

runtime = datetime.datetime.now() - t
print(runtime)
