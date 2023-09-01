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
from challenge64_Odd_period_square_roots import calcPeriodicSequenceForSquareRoot


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

Dsequences = [[1],[1]]

maxX = 0
maxD = 0
for number in range (2, 1001):
    Dsequences.append(calcPeriodicSequenceForSquareRoot(number))
    if int(math.sqrt(number))**2!=number:
        chainfraction = list(Dsequences[number][0:1])
        fraction = [1,1]
        i = 0


        while fraction[0]**2 - number*fraction[1]**2 != 1:
            fraction = fract(chainfraction)
            i += 1
            chainfraction.append(Dsequences[number][(((len(chainfraction)-1)%(len(Dsequences[number])-1))+1)])
        if fraction[0] > maxX:
            maxX = fraction[0]
            maxD = number
        print (number, fraction, maxX, maxD, fraction[0]**2-number*fraction[1]**2)

	
runtime = datetime.datetime.now() - t
print(runtime)

