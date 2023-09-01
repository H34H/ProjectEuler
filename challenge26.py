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
t = datetime.datetime.now()


intermediateResult = [313,337,361,367,379,383,389,419,433,461,487,491,499,503,509,529,541,571,577,593,601,619,626,631,647,653,659,667,674,677,683,701,709,713,719,722,727,731,734,743,749,758,761,766,778,787,791,799,811,821,823,827,833,838,839,841,857,863,866,877,881,883,887,893,899,911,917,919,922,929,937,939,941,947,953,961,967,971,974,977,982,983,989,991,998]
rep = True
def findRecurrence(Divisor):
	decimals = []
	strNumber = str(10**1000)
	remainder =[]
	step5 = Divisor
	i=0
	for i in range (0, len(strNumber)-1):
		if i==0:
			delen = divmod(int(strNumber[i]),Divisor)
		else:
			delen = divmod(step5,Divisor)
		decimals.append(delen[0])
		step3 = delen[0]*Divisor
		if i==0:
			step4 = int(strNumber[i])-step3
		else:
			step4 = step5-step3
		if step4 in remainder:
			break
		else:
			remainder.append(step4)
		step5 = step4*10+int(strNumber[i+1])
		i+=1
		decimalsResult = ""
		for i in decimals:
			decimalsResult+=str(i)
	return  decimalsResult

results = []
for i in intermediateResult:
	results.append((i, len(findRecurrence(i)),findRecurrence(i)))

resultsb  = [x for x in results if x[1] >=300]
resultsb.sort(key=lambda x: x[1])

for b in resultsb:
	print (b)




runtime  = datetime.datetime.now() - t
print (runtime)


