import datetime
import math
import sys
import itertools
import euler
import Eratosthenes
import copy
time = datetime.datetime.now()

factorial = {}
for i in range(0,10):
    factorial[i] = math.factorial(i)

def digitFactorial(number):
    sum = 0
    while number>0:
        sum += factorial[number%10]
        number = int(number/10)
    return sum

def cycleLength(number):
    perm = [number]
    repetition = False
    while repetition == False:
        number = digitFactorial(number)
        if number in perm:
            repetition = True
            return len(perm)
        else:
            perm.append(number)



sum = 0
for i in range(1, 10**6):
    a = cycleLength(i)
    if a==60:
        sum +=1
    
print (sum)
runtime  = datetime.datetime.now() - time
print (runtime)

###