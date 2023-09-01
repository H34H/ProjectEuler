import datetime
import math
import sys
import itertools
t = datetime.datetime.now()

n = 3
IsPrime = False
primes = []
primes.append(2)

while len(primes) < 10001:
	IsPrime = False
	for i in primes:
		#print (n,i)
		if i > math.sqrt(n):
			IsPrime = True
		else:
			if n%i==0:
				IsPrime = False
				break
	if IsPrime:
		primes.append(n)
		#print (n)
	n +=2
print (len(primes))
print (primes)
runtime  = datetime.datetime.now() - t
print (runtime)

###