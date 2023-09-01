import datetime
import os
from math import inf, lcm, log10
time = datetime.datetime.now() 

with open("Project Euler/0099_base_exp.txt", encoding='UTF-8') as f:
    t = f.readlines()

numbers = [list(map(int, x.strip().split(","))) for x in t]

largest = [1,1]

for idx, n in enumerate(numbers):
    if n[1] * log10(n[0]) > largest[1] * log10(largest[0]):
        largest = n
        print (idx+1, largest)
