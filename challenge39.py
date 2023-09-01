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
tsum = 0
pythresult = []

def most_common(L):
  # get an iterable of (item, iterable) pairs
  SL = sorted((x, i) for i, x in enumerate(L))
  # print 'SL:', SL
  groups = itertools.groupby(SL, key=operator.itemgetter(0))
  # auxiliary function to get "quality" for an item
  def _auxfun(g):
    item, iterable = g
    count = 0
    min_index = len(L)
    for _, where in iterable:
      count += 1
      min_index = min(min_index, where)
    # print 'item %r, count %r, minind %r' % (item, count, min_index)
    return count, -min_index
  # pick the highest-count/earliest item
  return max(groups, key=_auxfun)[0]

for a in range(1,500):
	for b in range (a,500):
			if int(math.sqrt(a**2+b**2))==math.sqrt(a**2+b**2) and a+b+int(math.sqrt(a**2+b**2))<1000:
				pyth = (a,b,int(math.sqrt(a**2+b**2)),a+b+int(math.sqrt(a**2+b**2)))
				pythresult.append(a+b+int(math.sqrt(a**2+b**2)))

print (most_common(pythresult))



runtime  = datetime.datetime.now() - t
print (runtime)


