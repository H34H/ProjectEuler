import datetime
import math

def prodList(myList) :
    result = 1
    for x in myList:
         result = result * x 
    return result 

getal = 1
a = 1
max = 100000
t = datetime.datetime.now()
result = []
E = []
rad = []

for getal in range (1, max+1):	
	a = getal
	b = 2
	while a%2==0:
	  a = a/2
	  rad.append(2)
	for b in range(3, int(math.sqrt(getal))+1,2):
	  while a%b == 0:
	  	a = a/b
	  	rad.append(b)
	if a > 2: 
		rad.append(int(a)) 
	#print (set(rad))
	E.append([getal, prodList(rad), prodList(set(rad))])
	rad = []
#E.sort(key=lambda x: x[0])
E.sort(key=lambda x: x[2])

#print (E)
print (E[10000-1])
runtime  = datetime.datetime.now() - t
print (runtime)  
