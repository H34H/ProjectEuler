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
tsum = 1

for a in range(10, 100):
	for b in range (a,100):
		for c in range (1,10):
			if str(c) in str(a) and str(c) in str(b):
				cancelledFractionNumerator = int(str(a).replace(str(c), '',1))
				cancelledFractionDenominator = int(str(b).replace(str(c), '',1))
				try:
					cancelledFraction = cancelledFractionNumerator/cancelledFractionDenominator
				except ZeroDivisionError:
					cancelledFraction = 0
				
				if cancelledFraction == a/b and cancelledFraction < 1:
					print ('{} / {} = {} = {} / {}'.format(a, b, a/b, cancelledFractionNumerator, cancelledFractionDenominator))
					tsum *= a/b
print (tsum)



runtime  = datetime.datetime.now() - t
print (runtime)


