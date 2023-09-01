import datetime
import math
import sys
import itertools
t = datetime.datetime.now()

cmax = 2
for n in range(2, 1000000):
	g = n
	c = 2
	while n > 1:
		if n%2==0:
			n = n/2 
		else:
			n = 3*n + 1
		c += 1
		#print (n)
	if c > cmax:
		cmax = c
		print (g, c)
runtime  = datetime.datetime.now() - t
print (runtime)

###