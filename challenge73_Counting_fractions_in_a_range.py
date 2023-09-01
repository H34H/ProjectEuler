import datetime
import math
import sys
import itertools
import euler
import Eratosthenes
import copy
time = datetime.datetime.now()


teller =0
for i in range (3, 12*10**3+1):
    lB = int(i/3)+1
    uB = int(i/2)+1
    for j in range (lB, uB):
        if math.gcd(i,j)==1:
            teller +=1
print (teller)
runtime  = datetime.datetime.now() - time
print (runtime)

###