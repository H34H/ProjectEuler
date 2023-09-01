import datetime
import math
import sys
import itertools
time = datetime.datetime.now()



with open('p067_triangle.txt') as f:
    t = f.readlines()
t = [x.strip() for x in t] 
t = [list(map(int,x.split(" "))) for x in t] 

r = len(t)-2
for r in range(r,-1,-1):
	for i in range(0, len(t[r])):
		a = t[r][i]+t[r+1][i]
		b = t[r][i]+t[r+1][i+1]
		if a>b:
			t[r][i] = a
		else:
			t[r][i] = b
	print (t[r])	

runtime  = datetime.datetime.now() - time
print (runtime)

###