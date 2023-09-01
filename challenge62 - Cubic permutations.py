import datetime
import math
import sys
import itertools
import copy
import csv
from fractions import Fraction
import matplotlib.pyplot
t = datetime.datetime.now()

cubic = {}

for i in range(0,10000):
    cubic[i] = (''.join(sorted(str(i**3))))

for i in range(0, len(cubic)):
    for j in range(i+1, len(cubic)):
        if cubic[i] == cubic[j]:
            for k in range(j+1, len(cubic)):
                if cubic[k] == cubic[j]:
                    for l in range(k+1, len(cubic)):
                        if cubic[l] == cubic[k]:
                            for m in range(l+1, len(cubic)):
                                if cubic[m] == cubic[k]:
                                    print (i, j, k, l, m, (i**3), cubic[j])
                                    exactFive = True
                                    #for n in range(m,len(cubic))


#print (cubic)
runtime  = datetime.datetime.now() - t
print (runtime)

import matplotlib.pyplot as plt
#plt.plot(approximation)
#plt.ylabel('approximation of e')
#plt.show()

