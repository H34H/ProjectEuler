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
tsum = 1
maxPandigitMultiple = 0


for i in range(1, 10**5):
    j = 1
    pandigital = True
    pandigitalMultiple = ''
    while pandigital:
        product = i * j
        #print (i, product)
        pandigitalMultiple += str(product)
        if len(set(pandigitalMultiple)) <= 9 and len(pandigitalMultiple) <= 9:
            if euler.isPandigitalNumber(pandigitalMultiple):
                if int(maxPandigitMultiple) < int(pandigitalMultiple):
                    maxPandigitMultiple = pandigitalMultiple
                    print(i, j, maxPandigitMultiple)
        else:
            pandigital = False
        j += 1


print(maxPandigitMultiple)


runtime = datetime.datetime.now() - t
print(runtime)
