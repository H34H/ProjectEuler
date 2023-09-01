import datetime
import math
import sys
import itertools
t = datetime.datetime.now()
ub = 11*13*14*15*16*17*18*19*20
candidates = []

def evaluateEvenDivisibility(number):
	divisible = False
	for i in range(2,20):
		if number%i == 0:
			#print (number, i, number/i)
			divisible = True
		else:
			#print (str(number)+' is not divisible by '+str(i))
			divisible = False
			break
	#rint (number, divisible)
	if divisible:
		for i in range(2,20):
			candidates.append(int(number/i))

	return divisible

candidates.append(ub)
max = ub
for c in candidates:
	if evaluateEvenDivisibility(c):
		if c < max:
			print(c)
			max = c



runtime  = datetime.datetime.now() - t
print (runtime)

###