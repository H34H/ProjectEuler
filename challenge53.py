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
def nCr(n,r):
    f = math.factorial
    return int(f(n) / f(r) / f(n-r))

for i in range (1,101):
	for j in range (1,i):
		k = nCr(i,j)
		print (i, j, k)
		if k > 10**6:
			teller +=1

print (teller)


runtime = datetime.datetime.now() - t
print(runtime)

