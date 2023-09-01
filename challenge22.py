import datetime
import math
import sys
import itertools
import copy
import csv
t = datetime.datetime.now()




#data inlezen
names = []
name = ''
with open('p022_names.txt') as f:
    names = f.readlines()
name = list(csv.reader(names[0].split(',')))



name.sort()
totalNameValue = 0
for idx, i in enumerate(name):
	nameValue = 0
	for j in i[0]:
		nameValue += (ord(j)-64)
	nameValue *= (idx+1)
	totalNameValue += nameValue
	i.append(nameValue)
	i.append(totalNameValue)
	#print (i)



#print (name[0])
#for idx, name in enumerate(names):
#	print (name)




runtime  = datetime.datetime.now() - t
print (runtime)

###