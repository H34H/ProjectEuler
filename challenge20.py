import datetime
import math
import sys
import itertools
import Eratosthenes

time = datetime.datetime.now()

primes = []



getal = 72
for i in Eratosthenes.get_primes(int(math.sqrt(getal))+1):
	primes.append(i)
divisor = 0
for divisor in primes:
	m=1
	deelbaar=True
	while deelbaar:
		#print (getal, divisor, m)
		if getal%(divisor*m)==0:
			print (divisor*m)
			m *=2
		else:
			deelbaar = False

#print(primes)

runtime  = datetime.datetime.now() - time
print (runtime)

###