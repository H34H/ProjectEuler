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
products = []

for i in range (1, 2000):
	for j in range (1,100):
		numbers = str(i)+str(j)+str(i*j)
		if len(numbers)==9 and len(set(numbers))==9 and not('0' in numbers):
			print ('{}*{}={}'.format(i,j,i*j))
			products.append(i*j)

print (sum(set(products)))

#print (tsum)


runtime  = datetime.datetime.now() - t
print (runtime)


