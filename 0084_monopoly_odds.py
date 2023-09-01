import datetime
import os
from math import inf, lcm, log10, sqrt
import Eratosthenes
import random
time = datetime.datetime.now() 

board = {0:'GO',1:'A1',2:'CC1',3:'A2',4:'T1',5:'R1',6:'B1',7:'CH1',8:'B2',9:'B3',10:'JAIL',11:'C1',12:'U1',13:'C2',14:'C3',15:'R2',16:'D1',17:'CC2',18:'D2',19:'D3',20:'FP',21:'E1',22:'CH2',23:'E2',24:'E3',25:'R3',26:'F1',27:'F2',28:'U2',29:'F3',30:'G2J',31:'G1',32:'G2 ',33:'CC3',34:'G3',35:'R4',36:'CH3',37:'H1',38:'T2',39:'H2'
}
communityChest = {1:'Advance to GO', 2:'Go to JAIL'}
communityChestOrder = list(range(16))
chance = {1:'Advance to GO',2:'Go to JAIL',3:'Go to C1',4:'Go to E3',5:'Go to H2',6:'Go to R1',7:'Go to next R',8:'Go to next R',9:'Go to next U',10:'Go back 3 squares'}
chanceOrder = list(range(16))

def nextMove(currentPos, instruction):
    if instruction == 'Advance to GO':
        return 1
    elif instruction == 'Go to JAIL':
        return 11
    elif instruction == 'Go to E3':
        return 25
    elif instruction == 'Go to H2':
        return 39
    elif instruction == 'Go to R1':
        return 6
    elif instruction == 'Go to next R':
        return (((currentPos+5)//10)*10+5)%40
    elif instruction == 'Go to next U':
        if currentPos > 12 and currentPos < 28:
            return 28
        else:
            return 12 
    elif instruction == 'Go back 3 squares':
        return (currentPos-3)%40
    
print(chanceOrder)
random.shuffle(chanceOrder)
random.shuffle(communityChestOrder)
print (communityChestOrder)





runtime  = datetime.datetime.now() - time
print (runtime)
