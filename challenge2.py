a, b, sum = 0, 1, 0
while a < 4000000:
	if a%2 == 0:
		sum = sum + a
		print(str(a) + '\t' + str(sum))
	a, b = b, a+b