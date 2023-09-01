import datetime
import os
from math import inf, lcm, log10, sqrt
import Eratosthenes

time = datetime.datetime.now() 
with open("Project Euler/0102_triangles.txt", encoding='UTF-8') as f:
    t = f.readlines()

t = [list(map(int,x.strip().split(','))) for x in t]

p = 0
inside, outside = 0,0
for x1, y1, x2, y2, x3, y3 in t:
    areaTriangle = abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1-y2))/2
    areaP12 = abs(x1*y2 + x2*-y1)/2
    areaP23 = abs(x2*y3 + x3*-y2)/2
    areaP13=  abs(x1*-y3 + x3*y1)/2
    if (areaTriangle == areaP12+areaP13+areaP23):
        inside += 1
    else:
        outside +=1
    #print (x1,y1, x2,y2,x3,y3, areaTriangle,areaP12+areaP13+areaP23, areaTriangle == areaP12+areaP13+areaP23)
print (inside, outside)
runtime  = datetime.datetime.now() - time
print (runtime)
