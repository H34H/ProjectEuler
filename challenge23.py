import datetime
import math
import sys
import itertools
import copy
import csv
t = datetime.datetime.now()
div = []
idiv = {}
maxrange = 28123
answer = 0

def canBeCalculatedbyAbundance(number):
	for j in range(0, len(idiv)):
		for k in range (j, len(idiv)):
			if idiv[j][0]+idiv[k][0] == number:
				#print (idiv[j][0],idiv[k][0],i)
				return Truepi
			if idiv[j][0]+idiv[k][0] > number:
				break
	return False

def canAbundance(number):
 	for i in idiv:
 		#print (i, number)
 		if number-idiv[i] in idiv:
 			#print (i, idiv[number-idiv[i]], number)
 			return True
 	return False



for i in range (0, maxrange):
	div = []
	for j in range(1, int(math.sqrt(i))+1):
		if i%j == 0:
			div.append(j)
			if j>1 and j != int(i/j):
				div.append(int(i/j))
	if sum(div)>i:
		idiv[i] = i
	del div

for i in range (1, maxrange):
	if canAbundance(i) == False:
		answer += i
		#print (i)

print (answer)
#print (idiv)
print (len(idiv))

runtime  = datetime.datetime.now() - t
print (runtime)


