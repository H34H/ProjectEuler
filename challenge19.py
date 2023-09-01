import datetime
import math
import sys
import itertools
import copy
import csv
t = datetime.datetime.now()

teller = 0

x = datetime.datetime(1901, 1, 1)

while x < datetime.datetime(2001,1,1):
	x += datetime.timedelta(days=1)
	if x.weekday() == 6 and x.day==1:
		teller +=1
	#print (x.weekday())

print(teller)



runtime  = datetime.datetime.now() - t
print (runtime)

###