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

pandigits = ['1','2','3','4','5','6','7']
teller = 0
pandigitsCandidates = []
for i in itertools.permutations(pandigits):
	number = int(''.join(i))
	pandigitsCandidates.append(number)
	teller +=1

pandigitsCandidates.sort

pandigitsCandidates = pandigitsCandidates[::-1]
primeFound = False
i = 0
while primeFound == False and i < len(pandigitsCandidates)-1:
	if euler.isPrime(pandigitsCandidates[i]):
		print (pandigitsCandidates[i])
		primeFound = True
	else:
		i +=1
	#print (pandigitsCandidates[i])

runtime = datetime.datetime.now() - t
print(runtime)
