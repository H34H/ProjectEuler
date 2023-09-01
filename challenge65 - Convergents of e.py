import datetime
import math
import sys
import itertools
import copy
import csv
from fractions import Fraction
import matplotlib.pyplot
t = datetime.datetime.now()

approximation = []

conFracE = [2,1,2]
Estep = 4
for i in range(1,99):
    if i%3 == 0:
        conFracE.append(Estep)
        Estep +=2
    else:
        conFracE.append(1)
print (conFracE)

for iteraties in range(0,10):
    nominator = 1
    denominator = conFracE[iteraties]
    #print (iteraties, conFracE[iteraties])

    for i in range (iteraties-1,-1,-1):
        #gcd = math.gcd(denominator,conFracE[i])
        denominator = denominator * conFracE[i]
        nominator = nominator*conFracE[i] + conFracE[i]*denominator
        if i > 0:
            nominator, denominator = denominator, nominator

    som = 0
    for i in str(int(nominator/math.gcd(nominator, denominator))):
        som += int(i)

    print (int(nominator/math.gcd(nominator, denominator)), int(denominator/math.gcd(nominator, denominator)), nominator/denominator, som)
    approximation.append(nominator/denominator)
print (math.gcd(nominator, denominator), int(nominator/6963524437876961749120273824619538346438023188214475670667))

som = 0
for i in str(6963524437876961749120273824619538346438023188214475670667):
    som += int(i)
print (som)
runtime  = datetime.datetime.now() - t
print (runtime)

import matplotlib.pyplot as plt
plt.plot(approximation)
plt.ylabel('approximation of e')
plt.show()

