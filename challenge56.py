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
maxNumber = 0

for a in range(1,100):
	for b in range(1,100):
		number = sum(list(map(int,str(a**b))))
		if number > maxNumber:
			maxNumber = number
print (maxNumber)

runtime = datetime.datetime.now() - t
print(runtime)

