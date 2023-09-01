import datetime
import math
import sys
import itertools
import copy
import csv
t = datetime.datetime.now()
numbers = [0,1,2,3,4,5,6,7,8,9]

a = itertools.permutations(numbers)
teller = 1
for i in a:
	if teller == 10**6:
		print (i)
		#break
	teller += 1
print (teller)

runtime  = datetime.datetime.now() - t
print (runtime)


