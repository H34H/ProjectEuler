import datetime
import math
from math import sqrt
import sys
import itertools
import copy
import collections
import operator
import euler
from operator import itemgetter
from decimal import Decimal
import Eratosthenes
t = datetime.datetime.now()

concatinatedPrimeCandidates = []
primes = {}
prime = []
intermediateResults = []
intermediateResults2 = []
for i in Eratosthenes.get_primes((8400)):
	prime.append(i)
for i in Eratosthenes.get_primes((9*10**7)):
	primes[i] = i

def convertToList(candidates):
	return (set([item for sublist in candidates for item in sublist]))

def concatPrimes(number1, number2):
	return int(str(number1)+str(number2))

def checkConcatinatedPrimeCandidate(prime, candidate):
	for c in candidate:
		if ((concatPrimes(c,prime) in primes)==False) or ((concatPrimes(prime,c) in primes)==False):
			return 0
	return 1

def checkConcatinatedPrime(candidatePrimes, candidate):
		#intermediateResults2 = []
		for p in candidatePrimes:
			if checkConcatinatedPrimeCandidate(p, candidate) == 1:
				evaluatedCandidate = (sorted([p] + candidate))
				#print (evaluatedCandidate)
				intermediateResults2.append(evaluatedCandidate)


def checkCandidates(candidates):
	candidatePrimes = convertToList(candidates)
	for candidate in candidates:
		checkConcatinatedPrime(candidatePrimes, candidate)

	intermediateResults2.sort()
	return (list(intermediateResults2 for intermediateResults2,_ in itertools.groupby(intermediateResults2)))

for j in prime:
	intermediateResults.append([j])

i1 = (checkCandidates(intermediateResults))
intermediateResults2 =[]
print (i1)
i2 = (checkCandidates(i1))
intermediateResults2 =[]
print (i2)
i3 = (checkCandidates(i2))
intermediateResults2 = []
print (i3)
i4 = checkCandidates(i3)
print (i4)


runtime = datetime.datetime.now() - t
print(runtime)

