import datetime
import math
from math import sqrt
import sys
import itertools
import copy
import csv
import decimal
from operator import itemgetter
from decimal import Decimal
import Eratosthenes

t = datetime.datetime.now()

#define Fibonacci
f = []
f.append(1)
f.append(1)
for j in range(0,90):
    f.append(f[j]+f[j+1])
#print (f)

#terugkerend patroon voor begincijfers; 39 = start[0]
start = []
start.append(10)
start.append(14)
start.append(19)
start.append(25)
start.append(32)
start.append(40)
start.append(49)
start.append(59)
start.append(79)
#1, 1, 2, 3, 5, 8, 13, 21, 34
fSum = [0,1,3,6,10,15,21,28,36,45,64,93,132,182,240,309,388,477,576,775,1074,1473,1972,2571,3270,4069,4968,5967,7966,10965,14964,19963,25962,32961,40960,49959,59958,79957,109956]
sTotal = 0
for i in f[1:91]:
    #nines = i // 9
    #remainder = i%9
    #s = int(str(remainder)+nines*'9')
    #sTotal.append(s)
    n=0
    if i > 37:
        #sNumber = int(str(start[(i-38)%9]) + str(int((((i-38)//9+4)*'9'))-i-5))
        #n = 10**((i-38)//9+5)
        sNumber = start[(i-38)%9]*10**((i-38)//9+5) -i -6
    else:
        sNumber = fSum[i]
    sTotal += sNumber
    print (i)
    

print (sTotal%1000000007)





# met elke 9 iteraties komt er 1 9 bij

#achterkant telt af 0 = -6
#for i in f:
#    print(i)



runtime  = datetime.datetime.now() - t
print (runtime)


