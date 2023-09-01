import datetime
import math
from math import sqrt
import sys
import itertools
import copy
import collections
import operator
import euler
from operator import itemgetter
from decimal import Decimal
import Eratosthenes

t = datetime.datetime.now()
maxNumber = 0

#uitgebreid algoritme van Euclides
def fract(con): 
      r, p = 0, 1 
      s, q = 1, 0 
      for i in con: 
          r, p = p, r + i * p 
          s, q = q, s + i * q 

      return (p, q) 

teller = 0
chainfraction = [1,2]
for i in range(1000):
	fraction = fract(chainfraction)
	if int(math.log10(fraction[0]))>int(math.log10(fraction[1])):
		teller+=1
	#print (teller, fraction, fraction[0]/fraction[1])
	chainfraction.append(2)
	
print (teller)
runtime = datetime.datetime.now() - t
print(runtime)

