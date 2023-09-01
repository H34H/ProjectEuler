import datetime
import math
import sys
import itertools
import euler
import Eratosthenes
import copy
from decimal import *

time = datetime.datetime.now()

getcontext().prec = 102
total = 0
i = 0
teller = 0
while i < 1000:
    if int(math.sqrt(i))**2==i:
        print (i)
    else:
        a = str(Decimal(i).sqrt())
        if math.sqrt(i)<10:
            b = sum(map(lambda x:int(x), a[2:101])) + int(a[0])
        else:
            b = sum(map(lambda x:int(x), a[3:102])) + int(a[0]) + int(a[1])
        total += b
        print(i, teller, b, len(a[2:101]), total, a[2:101])
        teller +=1
    i+=1
print (i, total, total/teller)

getcontext().prec = 100
a = (str(Decimal(2).sqrt()))
#print (a)
#print(sum(map(lambda x:int(x), a[2:101])))
getcontext().prec = 101
a = (str(Decimal(2).sqrt()))
#print (a)
#print(sum(map(lambda x:int(x), a[2:101])))

runtime  = datetime.datetime.now() - time
print (runtime)

###