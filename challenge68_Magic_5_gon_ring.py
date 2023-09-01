import datetime
import math
import sys
import itertools
time = datetime.datetime.now()

def intToString (list):
    return ''.join(str(x) for x in list)

for total in range (8,19):
    combinations = []
    for i in range (1,total+1):
        for j in range(1,total-i):
            k = total-(i+j)
            if (i!=j and j!=k and k!=i):
                combinations.append([i,j,k])
    if len(combinations) >=3:        
        maxDigitString = 0
        ringFound = False
        iTeller = 0
        externalNode = 0
        while (ringFound == False or externalNode >= combinations[iTeller][0]) and iTeller <= len(combinations)-1:
            i = combinations[iTeller]
            for j in list(filter(lambda x:x[1]==i[2] and not(x[0] in i) and not(x[2] in i),combinations)):
                for k in list(filter(lambda x:x[1]==j[2] and not(x[0] in i) and not(x[0] in j) and not(x[2] in i) and not(x[2] in j),(combinations))):
                    for l in list(filter(lambda x:x[1]==k[2] and not(x[0] in i) and not(x[0] in j)  and not(x[0] in k) and not(x[2] in i) and not(x[2] in j)  and not(x[2] in k),(combinations))):
                        for m in list(filter(lambda x:x[1]==l[2] and x[2]==i[1] and not(x[0] in i) and not(x[0] in j) and not(x[0] in k) and not(x[0] in l),(combinations))):
                            digitString = int(intToString(i)+intToString(j)+intToString(k)+intToString(l)+intToString(m))
                            if digitString > maxDigitString:
                                maxDigitString = digitString
                                externalNode = i[0]
                                ringFound = True
            iTeller += 1
        if maxDigitString > 0:
            print (total, maxDigitString, len(str(maxDigitString)))
        else:
            print ("geen oplossing voor: ", total)
    else:
        print ("geen oplossing voor: ", total)


runtime  = datetime.datetime.now() - time
print (runtime)

###