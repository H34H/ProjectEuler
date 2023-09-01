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
t = datetime.datetime.now()
result = [1]
k = 1

for i in range(2,1002,2):
	for j in range (1,5):
		k +=i
		print (k)
		result.append(k)

print (len(result),sum(result))

runtime  = datetime.datetime.now() - t
print (runtime)


