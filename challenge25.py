import datetime
import math
from math import sqrt
import sys
import itertools
import copy
import csv
import decimal
from decimal import Decimal
t = datetime.datetime.now()
a = 1
b = 1
lenF = 0
decimal.getcontext().prec = 100000
def F(a,b):
	return a+b
i = 3
lenf = 0
while lenF<1000:	
	lenF = len(str(F(a,b)))
	print (i, lenF, F(a,b))
	c = b
	b = F(a,b)
	a = c

	i += 1
print (i, lenf, F(a,b))


runtime  = datetime.datetime.now() - t
print (runtime)


