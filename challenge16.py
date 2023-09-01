import datetime
import math
import sys
import itertools
t = datetime.datetime.now()

p = str(2**1000)
sum = 0
for i in p:
	sum += int(i)
print (sum)
runtime  = datetime.datetime.now() - t
print (runtime)

###