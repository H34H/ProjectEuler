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

tsum = 0
for a in range(1, 10**6,2):
		b = "{0:b}".format(a)
		if str(a) == str(a)[::-1] and b == b[::-1]:
			print (a, "{0:b}".format(a))
			tsum += a

print (tsum)



runtime  = datetime.datetime.now() - t
print (runtime)


