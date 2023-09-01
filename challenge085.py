import datetime
import os
from math import inf, lcm, log10, sqrt

import Eratosthenes

time = datetime.datetime.now() 


closestRectangleSum = 0
x = 3
y = 3

smallestDiff = inf


#while rectangleSum =< 2*10**6+10000:

for y in range(3,1000):
    prevDiff = inf
    currentDiff = 2*10**6
    x = 1
    while currentDiff < prevDiff:
        rectangleSum = (x*(x+1)//2) * (y*(y+1)//2)
        prevDiff = currentDiff
        currentDiff = abs(2*10**6-rectangleSum)
        if currentDiff < smallestDiff:
            print (x, y, x*y, rectangleSum, smallestDiff)
            smallestDiff = currentDiff
        x+=1

        

runtime  = datetime.datetime.now() - time
print (runtime)
