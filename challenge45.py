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
tsum = 0

triangle = {}
pentagonal = {}
hexagonal = {}
for n in range(1, 10**6):
	triangle[int(n*(n+1)/2)] = n
	pentagonal[int(n*(3*n-1)/2)] = n
	hexagonal[int(n*(2*n-1))] = n

for i in triangle:
	#print (i)
	if i in pentagonal and i in hexagonal:
		print (i, triangle[i], pentagonal[i], hexagonal[i])



print (tsum)

runtime = datetime.datetime.now() - t
print(runtime)
