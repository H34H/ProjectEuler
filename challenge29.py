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

result = []
for a in range(2,101):
	for b in range(2,101):
		result.append(a**b)

print (len(result))
print (len(set(result)))
print ('')
runtime  = datetime.datetime.now() - t
print (runtime)


