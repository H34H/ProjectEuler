import datetime
import math
import sys
import itertools
t = datetime.datetime.now()

i = 0
triangel = 0

maxdiv=1
divisor = []
while maxdiv < 250:
	del divisor
	divisor=[]
	i += 1
	triangel += i
	factor=1
	tot = triangel
	divisors = 0
	while factor < math.sqrt(tot):	
		if tot%factor == 0:
			divisors +=1
			divisor.append(factor)
			#print(str(factor) + "\t" + (str(triangel)))
		factor += 1
	if divisors > maxdiv:
		print(int(triangel), divisor, divisors)
		maxdiv = divisors


runtime  = datetime.datetime.now() - t
print (runtime)

###