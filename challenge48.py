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
tsum = 0


for i in range(1, 10**3):
	tsum = tsum+(i**i)
		#break
tsum = str(tsum)
print (tsum[-10:])
#print (tsum)

runtime = datetime.datetime.now() - t
print(runtime)
