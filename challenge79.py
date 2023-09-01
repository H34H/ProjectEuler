import datetime
import math
import sys
import itertools
time = datetime.datetime.now()



with open('p079_keylog.txt') as f:
    t = f.readlines()
t = set([x.strip() for x in t])

codes = []
for x in t:
    x = [int(v) for v in x] 
    codes.append(x)

print (codes)
passcode = codes[0]

for i in range(1, len(codes)-1):
    if codes[i][0] == passcode[0] and codes[i][2] == passcode[1]:
        print (i)
    if codes[i][0] == passcode[1] and codes[i][2] == passcode[2]:
        print (i)
r1 = []
for x in codes:
    r1.append(x[0])

r2 = []
for x in codes:
    r2.append(x[1])

r3 = []
for x in codes:
    r3.append(x[1])

print (set(r1))
print (set(r2))
print (set(r3))

print (set(r1+r2+r3))

print (passcode)

runtime  = datetime.datetime.now() - time
print (runtime)

###