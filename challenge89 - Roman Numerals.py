import datetime
import math
import sys
import itertools
import copy
import csv
t = datetime.datetime.now()

with open('p089_roman.txt') as f:
    numbers = f.readlines()

numbers = [x.strip() for x in numbers]

roman = {}
roman['M'] = 1000
#roman['IM'] = 999
#roman['VM'] = 995
#roman['XM'] = 990
#roman['LM'] = 950
roman['CM'] = 900
roman['D'] = 500
#roman ['ID'] = 499
#roman['VD'] = 495
#roman ['XD'] = 490
#roman ['LD'] = 450
roman ['CD'] = 400
roman['C'] = 100
#roman['IC'] = 99
#roman['VC'] = 95
roman['XC'] = 90
roman['L'] = 50
#roman['IL'] = 49
#roman['VL'] = 45
roman['XL'] = 40
roman['X'] = 10
roman['IX'] = 9
roman['V'] = 5
roman['IV'] = 4
roman['I'] = 1

#Only one I, X, and C can be used as the leading numeral in part of a subtractive pair.
#I can only be placed before V and X.
#X can only be placed before L and C.
#C can only be placed before D and M.
#MCMLXXI 2171

def optimalNumeral(number):
    numerals = ''
    for i in roman:
        n  = int(number / roman[i])
        numerals += n*i
        number = number-n*roman[i]
   
    return numerals

def calculateArabicValue(romanNumeral):
    valueOfNumber = 0
    for i in range(0,len(romanNumeral)):
        if i+1 < len(romanNumeral):
            if roman[romanNumeral[i+1]] > roman[romanNumeral[i]]:
                valueOfNumber += roman[romanNumeral[i]+romanNumeral[i+1]]-roman[romanNumeral[i+1]]
            else:
                valueOfNumber += (roman[romanNumeral[i]])
        else:
            valueOfNumber += (roman[romanNumeral[i]])

    return valueOfNumber

originalLength = improvedLength = 0

for number in numbers:
   
    valueOfNumber = calculateArabicValue(number)
    optimalNumerals = optimalNumeral(valueOfNumber)
    #print(number + '\t' + str(valueOfNumber) + '\t' + str(optimalNumerals))
    originalLength += len(number)
    improvedLength +=len(optimalNumerals)

#print (originalLength)
#print (improvedLength)
print (originalLength - improvedLength)
runtime  = datetime.datetime.now() - t
print (runtime)


