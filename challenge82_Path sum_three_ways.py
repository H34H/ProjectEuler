import datetime
import math
import sys
import itertools
time = datetime.datetime.now()

def minimumSum(lst):
    ic = [x.index(min(x)) for x in lst] 
    ir = [min(x) for x in lst].index(min([min(x) for x in lst]))
    return ir, ic[ir], lst[ir][ic[ir]]

with open('p081_matrix.txt') as f:
    t = f.readlines()
t = [x.strip() for x in t] 
t = [list(map(int,x.split(","))) for x in t]



print (minimumSum(t))
#for r in range(1,80):
#    t[0][r] += t[0][r-1]
#    t[r][0] += t[r-1][0]

#for r in range(1,len(t)):
#	for c in range(1, len(t[r])):
#		if t[r-1][c]<t[r][c-1]:
#			t[r][c] += t[r-1][c]
#		else:
#			t[r][c] += t[r][c-1]
#print(t[79][79])

runtime  = datetime.datetime.now() - time
print (runtime)

###