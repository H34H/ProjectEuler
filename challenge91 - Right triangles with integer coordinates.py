import datetime
import math
import sys
import itertools
time = datetime.datetime.now()


def checkRightTriangle(x1,y1,x2,y2):

    OQ = x1**2+y1**2
    OP = x2**2+y2**2
    PQ = (x2-x1)**2+(y2-y1)**2

    if OQ==OP+PQ or OP==OQ + PQ or PQ==OQ + OP:
        return True
    else:
        return False


teller = 0
rightTriangle = []
for x1 in range(0,51):
    for y1 in range(x1,51):
        for x2 in range(0,51):
            for y2 in range(0,51):
                if not(x1 == x2 and y1 == y2) and not(x1 == 0 and y1==0) and not(x2==0 and y2==0):
                    if checkRightTriangle(x1,y1,x2,y2):
                        teller +=1
                        #rightTriangle.append([x1,y1,x2,y2])
                        #print (f"{x1}, {y1}, {x2}, {y2}, aantal rechte hoeken: {teller}")


#x1 = 1
#y1 = 0
#x2 = 0
#y2 = 1
#teller = checkRightTriangle(x1,y1,x2,y2)
print (f"aantal rechte hoeken: {teller}")

runtime  = datetime.datetime.now() - time
print (runtime)

###