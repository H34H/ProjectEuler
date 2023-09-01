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
pentagonalNumber = []
dictPentagonal = {}
for n in range(1,10**4):
	pentagonalNumber.append(int(n*(3*n-1)/2))
	dictPentagonal[int(n*(3*n-1)/2)]=int(n*(3*n-1)/2)

mindif = 10**6
for i in range(1, len(pentagonalNumber)):

	for j in range (i, len(pentagonalNumber)):
		#print(pentagonalNumber[i], pentagonalNumber[j], pentagonalNumber[i]+ pentagonalNumber[j])
		if abs(pentagonalNumber[i]-pentagonalNumber[j]) in dictPentagonal:
			pass#print ('verschil')
			if abs(pentagonalNumber[i]+pentagonalNumber[j]) in dictPentagonal:
				print(pentagonalNumber[i], pentagonalNumber[j], abs(pentagonalNumber[j]-pentagonalNumber[i]))
				if pentagonalNumber[j]-pentagonalNumber[i] <  mindif:
					print(pentagonalNumber[i]-pentagonalNumber[j], pentagonalNumber[j]-pentagonalNumber[i])
					mindif = abs(pentagonalNumber[j]-pentagonalNumber[i])
print (mindif)


print (tsum)

runtime = datetime.datetime.now() - t
print(runtime)
