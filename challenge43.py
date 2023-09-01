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
def checkSubstringDivisibility(number):
	ssd = {2:2,3:3,4:5,5:7,6:11,7:13,8:17}
	number = str(number)
	for i in range(1, len(number)-2):
		if int(number[i:i+3])%ssd[i+1]>0:
			return False
	return True

#print (checkSubstringDivisibility(1406357289))

pandigits = ['1','2','3','4','5','6','7','8','9','0']
teller = 0
pandigitsCandidates = []
j=0
for i in itertools.permutations(pandigits[:len(pandigits)-j:]):
	number = int(''.join(i))
	pandigitsCandidates.append(number)
	teller +=1

for k in pandigitsCandidates:
	if checkSubstringDivisibility(k):
		print (k)
		tsum+=k

print (tsum)

runtime = datetime.datetime.now() - t
print(runtime)
