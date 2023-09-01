import datetime
import math
import sys
import itertools
time = datetime.datetime.now()


squaredigit1 = {}
squaredigit89 = {}
squaredigit89[89] = 89
squaredigit1[1] = 1
teller89 = 0
teller1 = 0
a = 1

def SquareSum(n):
    k = 0
    while n>=1:
        m = n % 10
        n = int(n/10)
        k = k + m*m
    return k


for x in range (1,10**7):
    if x%10**5 == 0:
         print (x)
    if x in squaredigit89:
        teller89 +=1
    else:
        notPartOfSquareDigit = True
        #numberChain = [x]
        x = a
        while notPartOfSquareDigit == True:
            b = a
            a = SquareSum(a)
            #numberChain.append(a)
            if a in squaredigit89:
                teller89 += 1 
                squaredigit89[int(b)] = int(b)
                #numberChain.append(89)
                notPartOfSquareDigit = False
            if a  in squaredigit1:
                teller1 +=1
                squaredigit1[int(b)] = int(b)
                #numberChain.append(1)
                notPartOfSquareDigit = False
        #print (numberChain)
print ("89: \t"+ str(teller89))
print ("1:\t" + str(teller1))
runtime  = datetime.datetime.now() - time
print (runtime)

###