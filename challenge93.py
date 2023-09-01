import datetime
import math
import sys
import itertools
t = datetime.datetime.now()

a=1
b=2
c=3
d=4

g0,g1,g2,g3='','','',''
op1,op2,op3='','',''

A=[a,b,c,d]
operator = ['+','-','*','/']
lijst =[]
hk =[]
volgorde = []
op =[]


hk.append('str(g0)+op1+str(g1)+op2+str(g2)+op3+str(g3)')
hk.append('"("+str(g0)+op1+str(g1)+")"+op2+str(g2)+op3+str(g3)')
hk.append('"("+str(g0)+op1+str(g1)+op2+str(g2)+")"+op3+str(g3)')
hk.append('"(("+str(g0)+op1+str(g1)+")"+op2+str(g2)+")"+op3+str(g3)')
hk.append('"("+str(g0)+op1+"("+str(g1)+op2+str(g2)+"))"+op3+str(g3)')
hk.append('"("+str(g0)+op1+str(g1)+")"+op2+"("+str(g2)+op3+str(g3)+")"')
hk.append('str(g0)+op1+"("+str(g1)+op2+str(g2)+")"+op3+str(g3)')
hk.append('str(g0)+op1+"("+str(g1)+op2+str(g2)+op3+str(g3)+")"')
hk.append('str(g0)+op1+"(("+str(g1)+op2+str(g2)+")"+op3+str(g3)+")"')
hk.append('str(g0)+op1+"("+str(g1)+op2+"("+str(g2)+op3+str(g3)+"))"')
hk.append('str(g0)+op1+str(g1)+op2+"("+str(g2)+op3+str(g3)+")"')


def bepaalmaxreeks(res):
	reeks = 0
	maxreeks = 1

	x = 0
	y=-1
	for x in res:
		if x == y+1 or y==-1:
			reeks +=1
		else:
			break
		y=x
	return (reeks)

def calc(volgorde, op, haakje):
	try:
		g0 = str(volgorde[0])
		g1 = str(volgorde[1])
		g2 = str(volgorde[2])
		g3 = str(volgorde[3])
		op1,op2,op3=op[1],op[2],op[3]
		
		sum = float(eval(eval(haakje)))
		if sum.is_integer() and sum >0:
			#print (int(sum), eval(haakje))
			return int(sum)
		else:
			return 0
		pass
	except ZeroDivisionError as e:
		return 0


def heap_perm(A):
    n = len(A)
    Alist = [el for el in A]
    for hp in _heap_perm_(n, Alist):
        yield hp


def _heap_perm_(n, A):
    if n == 1: yield A
    else:
        for i in range(n-1):
            for hp in _heap_perm_(n-1, A): yield hp
            j = 0 if (n % 2) == 1 else i
            A[j],A[n-1] = A[n-1],A[j]
        for hp in _heap_perm_(n-1, A): yield hp

def maxreeks(G):
	del lijst[:]
	ax = []
	for volgorde in heap_perm(G):
		for op in itertools.product(operator, repeat=4):
			for haakje in hk:
				ax = calc(volgorde, op, haakje)
				if ax > 0:
					lijst.append(ax)

	res = (sorted(set(lijst)))
	return (G, bepaalmaxreeks(res))

#print (maxreeks(A))



abcd = []
teller = 0
endresult = []
for i in range(1,13):
	abcd.append(i)
for xx in itertools.permutations(abcd,4):
	if xx[0]<xx[1] and xx[1]<xx[2] and xx[2] < xx[3]:
		print (maxreeks(xx))
		endresult.append(maxreeks(xx))
		teller += 1

print (sorted(endresult, key=lambda x:x[1]))
runtime  = datetime.datetime.now() - t
print (runtime)

###