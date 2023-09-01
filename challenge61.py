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

def polygonalNumber(n,p):
	if p==3:
		return int(n*(n+1)/2)
	elif p==4:
		return n**2
	elif p==5:
		return int(n*(3*n-1)/2)
	elif p==6:
		return n*(2*n-1)
	elif p==7:
		return int(n*(5*n-3)/2)
	elif p==8:
		return n*(3*n-2)
	else:
		return 'Error!'

def extendChain(chain, pChecked):
	number = chain[-1]
	matched0 = list(filter(lambda x: x[2] == number[3], polygonalNumbers))
	matched = list(filter(lambda x: x[1] not in pChecked, matched0))
	if len(matched) == 0 and len(pChecked)==6 and number[3]==chain[0][2]:
		answer = sum([x[0] for x in chain])
		print (chain, pChecked, answer)
	else:
		for number in matched:
			extendChain(chain+[number], pChecked+[number[1]])

polygonalNumbers = []
for p in range(3,9):
	number = 0
	n = 0
	while number < 10000:
		number = polygonalNumber(n,p)
		if number > 1000 and number < 10000:
			if number%100 > 9:
				polygonalNumbers.append([number, p, int(number/100), number%100])
		n += 1

polygonalNumbers.sort()

for number in polygonalNumbers:
	extendChain([number], [number[1]])

runtime = datetime.datetime.now() - t
print(runtime)
