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


def checkStraight(hand):
    x = sorted([cardOrder[x[0]] for x in hand])
    if x[4] - x[3] == 1 and x[3] - x[2] == 1 and x[2] - x[1] == 1 and x[1] - x[0] == 1:
        return 'Straight', x[4]
    else:
        return 0,x[0]


def checkFlush(hand):
    x = sorted([cardOrder[x[0]] for x in hand])
    color = [x[1] for x in hand]
    if len(set(color)) == 1:
        if x[4] - x[0] == 4:
            if x[4] == 14:
                return 'Royal Flush'
            else:
                return 'Straight Flush', x[0]
        else:
            return 'Flush', x[0]
    else:
        return 0,x[0]


def checkFourofaKind(hand):
    x = sorted([cardOrder[x[0]] for x in hand])
    count = [[key, len(list(group))] for key, group in itertools.groupby(x)]
    count = sorted(count, key=itemgetter(1, 0), reverse=True)
    # print (hand, count)
    if count[0][1] == 4:
        return 'Four of a Kind', count[0][0]
    elif count[0][1] == 3 and count[1][1] == 2:
        return 'Full House', count[0][0]
    elif count[0][1] == 3:
    	return 'Three of a Kind', count[0][0]
    elif count[0][1] == 2 and count[1][1] == 2:
    	return 'Two Pairs', count[0][0]
    elif count[0][1] == 2:
    	return 'Pair', count[0][0]
    elif count[0][1] == 1:
    	return 'High Card', count[0][0] 



def determineHand(hand):
    x = sorted([cardOrder[x[0]] for x in hand])
    color = [x[1] for x in hand]
    straight = checkStraight(hand)
    flush = checkFlush(hand)
    nrOfKind = checkFourofaKind(hand) 
    if flush[0] == 'Royal Flush' or flush == 'Straight Flush':
        return flush
    if nrOfKind[0] == 'Four of a Kind':
    	return nrOfKind
    if nrOfKind[0] == 'Full House':
    	return nrOfKind
    if flush == 'Flush':
        return flush
    if straight[0] == 'Straight':
    	#print (hand, flush, straight)
    	return straight
    return nrOfKind


def determineWinner(handPlayer1, handPlayer2):
    hand1 = determineHand(handPlayer1)
    hand2 = determineHand(handPlayer2)
    winner = ''
    wins =0
    if handOrder[hand1[0]] > handOrder[hand2[0]]:
    	winner = 'Player 1 wins'
    	wins +=1
    else:
    	if handOrder[hand1[0]] == handOrder[hand2[0]]:
    		if hand1[1] > hand2[1]:
    			winner = 'Player 1 wins'
    			wins +=1
    		else:
    			winner = 'Player 2 wins'
    	else:
    		winner = 'Player 2 wins'
    #if hand1[0] == 'Straight' or hand2[0] == 'Royal Flush':
    print ('{} {:15} | {} {:15} {:15}'.format(handPlayer1, hand1[0], handPlayer2, hand2[0], winner))
    return (wins)

# data inlezen
with open('p054_poker.txt') as f:
    content = f.readlines()
hands = [x.strip().split(' ') for x in content]
player1 = []
player2 = []
for x in hands:
    player1.append(x[:5])
    player2.append(x[5:])

cardOrder = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
             '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
handOrder = {'High Card': 0, 'Pair': 1, 'Two Pairs': 2, 'Three of a Kind': 3, 'Straight': 4,
             'Flush': 5, 'Full House': 6, 'Four of a Kind': 7, 'Straight Flush': 8, 'Royal Flush': 9}
winner = 0
for i in range(0, 1000):
    winner += determineWinner(player1[i], player2[i])
print (winner)

runtime = datetime.datetime.now() - t
print(runtime)

# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
#+++Straight: All cards are consecutive values.
#+++Flush: All cards of the same suit.
#++ Full House: Three of a kind and a pair.
#+++Four of a Kind: Four cards of the same value.
#+++Straight Flush: All cards are consecutive values of same suit.
#+++Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
