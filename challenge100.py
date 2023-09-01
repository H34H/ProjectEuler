import datetime
import math
import sys
import itertools
import copy
import csv
t = datetime.datetime.now()
nrOfDiscs = 1070379110497
fractionHalf = []
#3119310671123
#1000000000000
#3119310671123 estimate
#3119310671963 uitkomst 1
#3119310671161 uitkomst 2

teller = 1
probHalf = False
while probHalf == False:
    nrOfBlue = (1 + math.sqrt(2*nrOfDiscs**2 - 2*nrOfDiscs + 1))/2
    if nrOfBlue.is_integer():
   	    print (int(nrOfBlue), nrOfDiscs) #, nrOfBlue/nrOfDiscs)
   	    nrOfDiscs * 5
   	    if nrOfDiscs > 10**12:
   	    	probHalf = True
   	    	break
    nrOfDiscs += 1

print ((nrOfBlue/nrOfDiscs*((nrOfBlue-1)/(nrOfDiscs-1))).as_integer_ratio())

runtime  = datetime.datetime.now() - t
print (runtime)

#print ((707106802629/1000000030324)*(707106802628/1000000030323))

###