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
answer = 0
for i in range (2, 10**6):
	si = str(i)
	powerSum = 0
	for j in range (0, len(si)):
		powerSum += int(si[j])**5
	if i == powerSum:
		print (i, powerSum)
		answer += powerSum
print (answer)


runtime  = datetime.datetime.now() - t
print (runtime)


