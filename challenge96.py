import datetime
import math
import sys
import itertools
import copy
t = datetime.datetime.now()

def IsSudokuSolved(sudok):
	checksum = 0
	for i in sudok:
		for j in i:
			if type(j) is int:
				checksum += j
	if checksum == 405:
		return True
	else:
		return False

def fillZeroWithCandidates(su):
	for i in range(0,9):
		for j in range (0,9):
			if su[i][j] == 0:
				su[i][j] = [1,2,3,4,5,6,7,8,9]

def solveByLogic(sudok):
	#check veld voor veld
	iteratie = 0
	previouschecksum = 0 
	while iteratie < 10:
		for i in range(0,9):
			for j in range (0,9):
				check = su[i][j]
				if type(su[i][j]) is list:
					#check row
					for y in range (0,9):
						if not(type(su[i][y]) is list):
							try:
								su[i][j].remove(su[i][y])
							except:
								pass
					#check column:
					for x in range (0,9):
						if not(type(su[x][j]) is list):
							try:
								su[i][j].remove(su[x][j])
							except:
								pass
					#check blok:
					bx = int(i/3)
					cy = int(j/3)
					for x in range (bx*3,bx*3+3):
						for y in range (cy*3,cy*3+3):
							if not(type(su[x][y]) is list):
								try:
									su[i][j].remove(su[x][y])
								except:
									pass #print (su[x][y])
					#check of nummer als enige nog voorkomt in rij / kolom / vak
					for candidate in su[i][j]:
						#check rij
						occurence = 0
						for column in range (0,9):
							if type(su[i][column]) is list:
								if candidate in su[i][column]:
									occurence +=1
						if occurence==1 and not(type(su[i][j]) is int):
							su[i][j] = candidate
						
						#check kolom
						occurence = 0
						for row in range (0,9):
							if type(su[row][j]) is list:
								if candidate in su[row][j]:
									occurence +=1
						if occurence==1 and not(type(su[i][j]) is int):
							su[i][j] = candidate

						#check vak
						occurence = 0
						bx = int(i/3)
						cy = int(j/3)
						for row in range (bx*3,bx*3+3):
							for column in range (cy*3,cy*3+3):						
									if type(su[row][column]) is list:
										if candidate in su[row][column]:
											occurence +=1
						if occurence==1 and not(type(su[i][j]) is int):
							su[i][j] = candidate

					#nummer gevonden: vul in
					if type(su[i][j]) is list:
						if len(su[i][j])==1 and type(su[i][j]) is list:
							su[i][j] = su[i][j][0]
		if IsSudokuSolved(su) == True:
			break
		iteratie +=1

def selectGuess(sudok):
	for i in range(0,9):
		for j in range(0,9):
			if type(sudok[i][j]) is list:
				if len(sudok[i][j])>0:
					#print ('candidates:\t' + str(sudok[i][j]) + ' \t guess: \t' + str(sudok[i][j][0]))
					return i,j, sudok[i][j][0]
				else:
					return (0,0,0)

def tryGuess(sudok, row, column, guess):
	sudok[row][column] = guess
	solveByLogic(sudok)


#data inlezen
solved = 0 
euler = 0
with open('p096_sudoku.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content] 

sudoku = []*50
for s in sudoku:
	s = []*10
for s in sudoku:
	for c in s:
		c = []

su = 0
for s in range(0, len(content)):
	l = content[s]
	if l[:4]=='Grid':
		sudoku.append([])
		for r in range(1,10):
			c =[]
			for co in content[s+r]:
				c.append(int(co))
			sudoku[su].append(c)
		su +=1


for idx, su in enumerate(sudoku):
	stimer = datetime.datetime.now()
	# vul alle mogelijkheden voor lege waarden
	fillZeroWithCandidates(su)
	
	# los zover mogelijk op met logica
	solveByLogic(su)
	
	candidateguess = []*4
	guessTree = []
	stepDetails = []
	while IsSudokuSolved(su) == False:
		#selecteer de gok indien mogelijk
		candidateguess = selectGuess(su)
		#voeg extra gok toa aan de boom als dat kan ga anders een stap terug
		if candidateguess != (0,0,0):
			stepDetails = (copy.deepcopy(su), candidateguess[0], candidateguess[1], su[candidateguess[0]][candidateguess[1]],su[candidateguess[0]][candidateguess[1]][0])
			guessTree.append(stepDetails)
		else:
			#guess werkt niet, terug naar vertrekpunt
			if len(guessTree[-1][3]) <= 1:
				del guessTree[-1]
			su = copy.deepcopy(guessTree[-1][0])
			#verwijder verkeerde gok uit sudoku
			su[guessTree[-1][1]][guessTree[-1][2]].remove(guessTree[-1][4])	
			#verwijder candidate uit guesstree
			guessTree[-1][3].remove(guessTree[-1][4])
			#en probeer opnieuw
			candidateguess = selectGuess(su)		
		tryGuess(su, candidateguess[0], candidateguess[1], candidateguess[2])

	#start guessing
	# maak backup
	# vul bepaalde waarde in
	# test waarde
	# als ok: 
	#	ga door
	# zet bakcup terug, verwijder waarde

	# toon voortgang
	if IsSudokuSolved(su) == True:
		solved +=1
		print ("")
		print ('Sudoku: \t' + str(idx+1))
		euler += int(su[0][0]*100 + su[0][1]*10 + su[0][2])

		print 
		for i in su:
			for j in i:
				print (j, end="|")
			print ("")

	else:
		print ('NOT SOLVED:')
	print ('time needed:\t' + str(datetime.datetime.now() - stimer))

print ('Sudoku\'s solved: ' + str(solved))


runtime  = datetime.datetime.now() - t
print (runtime)

###