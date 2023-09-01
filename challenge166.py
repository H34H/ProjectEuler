#0,1 = 0,2 = 0,3, 1,2 = 34 oplossingen * 100 = 3400
#
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

def checkCross(c, sumRow):
	c0 = c[0][0]+c[1][0]+c[2][0]+c[3][0]
	c1 = c[0][1]+c[1][1]+c[2][1]+c[3][1]
	c2 = c[0][2]+c[1][2]+c[2][2]+c[3][2]
	c3 = c[0][3]+c[1][3]+c[2][3]+c[3][3]
	
	xl = c[0][0]+c[1][1]+c[2][2]+c[3][3]
	xr = c[0][3]+c[1][2]+c[2][1]+c[3][0]

	if sumRow == c0 and c0 == c1 and c1 == c2 and c2 == c3:
		if sumRow == xl and xl == xr:
			return True
		else:
			return False
		return True
	else:
		return False

def completeColumn(row1, row2, column, sumRow):
	remainder = sumRow-row1[column]-row2[column]
	if remainder >= 0 and remainder <=18:
		return completeColumnSum[remainder]
	else:
		return []

def checkRow(row, expectedResult):
	if sum(row)==expectedResult:
		return True
	else:
		return False

#genereer numbers
combis =[]
hcombis = {}
for i in itertools.product(range(10), repeat=4):
	a = list(i)
	combis.append(a)
	hcombis[i] = sum(i)

sumcombi = []
for i in range(37):
	a = [x for x in combis if sum(x)==i]
	sumcombi.append(a)

completeColumnSum = []
for i in range(19):
	x = []
	for a in range(10):
		for b in range(10):
			if a+b == i:
				x.append([a,b])
	completeColumnSum.append(x)


teller = 0
for i in range(19):
	for row1 in sumcombi[i]:
		sumRow1 = sum(row1)
		for row2 in sumcombi[sumRow1]:
			#check diagonalen
			if sumRow1 - (row1[0] + row2[1]) <= 18 and (row1[0] + row2[1]) <= sumRow1 and sumRow1 - (row1[3] + row2[2]) <= 18 and (row1[3] + row2[2]) <= sumRow1:
				for c1 in completeColumn(row1,row2, 0, sumRow1):
					if sumRow1 - c1[0] <= 27 and sumRow1 - c1[1] <= 27 and c1[0] <= sumRow1 and c1[1] <= sumRow1:
						for c2 in completeColumn(row1,row2, 1, sumRow1):
							if row1[3]+row2[2]+c2[0]+c1[1] == sumRow1:
								if sumRow1 - (c1[0]+c2[0]) <= 18 and sumRow1 - (c1[1]+c2[1]) <= 18 and c1[0]+c2[0] <= sumRow1 and c1[1]+c2[1] <= sumRow1:
									for c3 in completeColumn(row1,row2, 2, sumRow1):
										if sumRow1 - (row1[0] + row2[1] + c3[0]) <= 9 and (row1[0] + row2[1] + c3[0]) <= sumRow1:
											if sumRow1 - (c1[0]+c2[0]+c3[0]) <= 9 and sumRow1 - (c1[1]+c2[1]+c3[1]) <= 9 and c1[0]+c2[0]+c3[0] <= sumRow1 and c1[1]+c2[1]+c3[1] <= sumRow1:
												for c4 in completeColumn(row1,row2, 3, sumRow1):
													if row1[3]+row2[3]+c4[0]+c4[1]==sumRow1 and sum([c1[0], c2[0], c3[0], c4[0]])==sumRow1 and sum([c1[1], c2[1], c3[1], c4[1]]) == sumRow1 and row1[0]+row2[1]+c3[0]+c4[1]==sumRow1:			
														teller +=1					
														#print (row1)
														#print (row2)
														#print ([c1[0], c2[0], c3[0], c4[0]])
														#print ([c1[1], c2[1], c3[1], c4[1]])
														#print ('---')


		print (row1, teller)
print (teller)
runtime = datetime.datetime.now() - t
print(runtime)

#0,1,2,3 = 5400
#0,1,2 = 621
#0,1 = 34
#194848373
#4294967296
#range(4) in 0:00:01.270602