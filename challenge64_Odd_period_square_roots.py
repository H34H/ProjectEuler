import datetime
import math
import sys
import itertools
import copy
import csv
from fractions import Fraction
import matplotlib.pyplot
from decimal import *

t = datetime.datetime.now()


def calcPeriodicSequenceForSquareRoot(number):
    oddPeriodSquare = 0
    period = 0
    i =1
    a,x,xD, xN = [], [],[],[]
    hashX = {}
    if int(math.sqrt(number))**2==number:
         a.append(int(math.sqrt(number)))
    else:
        
        x.append(math.sqrt(number))
        #step 1
        a.append(int(x[0]))
        #step 2
        xN.append(1)
        xD.append(a[0])
        #step 3
        xN[0] = (xN[0]*a[0])
        xD[0] = number-a[0]**2

        #print (a[0], x[0], xN[0], xD[0], ((math.sqrt(number)+xN[0])/xD[0]))
        i = 1
        repeating = False
        while repeating == False:
            #step 1
            a.append(int((math.sqrt(number)+xN[i-1])/xD[i-1]))
            #step 2
            xNumerator = xD[i-1] 
            xDenumerator = xN[i-1]-xNumerator*a[i] 
            #step 3
            xN.append(xDenumerator*-1)
            xD.append(int((number - xDenumerator**2)/xNumerator))
            x.append((math.sqrt(number)+xN[i])/xD[i])

            
            #print (a[i], x[i], xN[i], xD[i], (math.sqrt(number)+xN[i])/xD[i])
            if 1000*xN[i]+xD[i] in hashX:
                repeating = True
                if (i-1)%2!=0 and i >1:
                    oddPeriodSquare += 1
            else:
                hashX[1000*xN[i]+xD[i]] = 1000*xN[i]+xD[i]
                i += 1
    if (len(a)>1):
        return a[0:-1] # print (number, i-1, a)
    else:
        return a

#for i in range (1, 100):
#    print (calcpPeriodicSequenceForSquare(i))

#print (oddPeriodSquare)

#runtime  = datetime.datetime.now() - t
#print (runtime)

import matplotlib.pyplot as plt
#plt.plot(approximation)
#plt.ylabel('approximation of e')
#plt.show()

