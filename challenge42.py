import datetime
import math
from math import sqrt
import sys
import itertools
import copy
import collections
import operator
import csv
import euler
from operator import itemgetter
from decimal import Decimal
import Eratosthenes
t = datetime.datetime.now()

#data inlezen
words = []
word = ''
with open('p042_words.txt') as f:
    words = f.readlines()
word = list(csv.reader(words[0].split(',')))

word2 = []
for i in word:
	word2.append((i[0].replace('"','')))

triangleNumbers = {}
j = 0
for i in range(0,100):
	j +=i
	triangleNumbers[j] = j

triangleWords = 0

for i in word2:
	wordValue = 0
	for j in i:
		wordValue += (ord(j)-64)
	#print (wordValue)
	if wordValue in triangleNumbers:
		print (i, wordValue)
		triangleWords +=1


print (triangleWords)

runtime = datetime.datetime.now() - t
print(runtime)
