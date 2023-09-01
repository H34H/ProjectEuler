import datetime
import math
import sys
import itertools
import copy
import csv
from fractions import Fraction
import matplotlib.pyplot
t = datetime.datetime.now()

teller = 0
for i in range(1,100):
    for j in range(0,100):
        if j == len(str(i**j)):
            #   print (i, j, i**j, len(str(i**j)))
            teller+=1
print (teller)

runtime  = datetime.datetime.now() - t
print (runtime)

import matplotlib.pyplot as plt
#plt.plot(approximation)
#plt.ylabel('approximation of e')
#plt.show()

