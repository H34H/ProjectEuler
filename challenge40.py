import datetime
import math
from math import sqrt
import sys
import itertools
import copy
import csv
import decimal
import collections
import operator
from operator import itemgetter
from decimal import Decimal
import Eratosthenes

t = datetime.datetime.now()
tsum = 1
champernowne = ''
i = 0
while len(champernowne)<1000001:
	champernowne += str(i)
	i +=1

for i in range (0,7):
	print(champernowne[10**i])
	tsum *= int(champernowne[10**i])

print (tsum)


runtime  = datetime.datetime.now() - t
print (runtime)


