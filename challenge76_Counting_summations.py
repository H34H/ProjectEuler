import datetime
import math
import sys
import itertools
import euler
import Eratosthenes
import copy

time = datetime.datetime.now()
getal = 100
teller = 0

def summation(goalNumber, pastNumber, remainder):
    global teller
    if remainder == 0:
        teller += 1
        #print("=", teller)
    else:
        for i in range(1, min(pastNumber,remainder)+1):
            #print (i, remainder)
            summation(goalNumber, i, remainder-i)

summation(getal,getal-1,getal)

print (teller)
        
runtime  = datetime.datetime.now() - time
print (runtime)

###