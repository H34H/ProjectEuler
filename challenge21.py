import datetime
import math
import sys
import itertools
import copy
import csv
t = datetime.datetime.now()
div = []
idiv = []
maxrange = 10001
for i in range (0, maxrange):
	div = []
	for j in range(1, i):
		if i%j == 0:
			div.append(j)
	idiv.append([i,sum(div)])
	del div
sumamic = 0
for d in range(1,maxrange-1):
	number = idiv[d][0]
	divsum = idiv[d][1]
	if divsum < maxrange and divsum > 1:
		if idiv[d][0] == idiv[idiv[d][1]][1]:
			if idiv[d][0] != idiv[d][1]:
				print (idiv[d], idiv[idiv[d][1]])
				sumamic += idiv[d][0]

print (sumamic)
runtime  = datetime.datetime.now() - t
print (runtime)


#print ((707106802629/1000000030324)*(707106802628/1000000030323))

###