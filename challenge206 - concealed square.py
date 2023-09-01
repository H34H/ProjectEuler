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

#1_2_3_4_5_6_7_8_9_0
lb = int(math.sqrt(1020304050607080900))
ub = int(math.sqrt(1929394959697989990))
for i in range (lb, ub+1, 10):
    j = str(i**2)
    if j[0] == '1' and j[2] == '2' and j[4] == '3' and j[6] == '4' and j[8] == '5' and j[10] == '6' and j[12] == '7' and j[14] == '8' and j[16] == '9':
        print (i,j)    
runtime  = datetime.datetime.now() - t
print (runtime)


