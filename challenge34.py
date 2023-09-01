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

f = []
for i in range (0,10):
	f.append(math.factorial(i))
tsum = 0

for i in range(10, f[9]*6):
	digit = str(i)
	fsumdigit = 0
	for j in range(0, len(digit)):
		fsumdigit += math.factorial(int(digit[j]))
		if fsumdigit == i:
			print (i)
			tsum += i

print (tsum)




runtime  = datetime.datetime.now() - t
print (runtime)


