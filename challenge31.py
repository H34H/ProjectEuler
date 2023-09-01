import datetime
import math
import sys
import itertools
import copy
import csv
t = datetime.datetime.now()
coins = []*8
"""for i in coins:
	i = []*100

for i in range(0, 8):
	coins.append([])

for i in range (0,1):
	coins[0].append(200)
for i in range (0,2):
	coins[1].append(100)
for i in range (0,4):
	coins[2].append(50)
for i in range (0,10):
	coins[3].append(20)
for i in range (0,20):
	coins[4].append(10)
for i in range (0,40):
	coins[5].append(5)
for i in range (0,100):
	coins[6].append(2)
for i in range (0,200):
	coins[7].append(1)"""
coins = [200,100,50,20,10,5,2,1]
#combination =[]
amountToPay = 200
global teller
teller = 0
combinations =[]
combination = []

def addCoins(coinle, currentAmount,thread):
	#bereken hoeveel keer deze munt maximaal in resterend bedrag past
	# probeer alle mogelijkheden toe te voegen
	callingAmount = currentAmount
	coin = coins[coinle]
	maxCoins = int((amountToPay-currentAmount) / coin)
	if(coin==1):
		thread.append(str(maxCoins)+'*$'+str(coin))
		currentAmount += maxCoins*coin
		combinations.append(thread)
	else:
		for nrOfCoins in range(0, maxCoins+1):
			currentAmount = callingAmount
			tak = copy.deepcopy(thread)
			addition = coin*nrOfCoins
			if coinle < len(coins)-1 and currentAmount+addition<amountToPay:
				if(nrOfCoins > 0):
					tak.append(str(nrOfCoins)+'*$'+str(coin))
					currentAmount += addition
					if currentAmount == amountToPay:
						#print (tak, currentAmount)
						combinations.append(tak)

				addCoins(coinle+1,currentAmount, copy.deepcopy(tak))
			else:
				currentAmount += addition
				if(nrOfCoins>0 and currentAmount <= amountToPay):
					tak.append(str(nrOfCoins)+'*$'+str(coin))
					#print(tak,currentAmount)
					combinations.append(tak)

		




addCoins(0,0,[])	
print (len(combinations))
#print (a)
	
#print(combination, sum, i, len(combinations))
#for combination in combinations:
#	print ((combination))

runtime  = datetime.datetime.now() - t
print (runtime)

###