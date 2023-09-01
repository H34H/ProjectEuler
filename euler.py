import math

def isPandigitalNumber(number = 0):
	length = len(str(number))
	if length == 10:
		return len(set(str(number))) == length and len(str(number)) == length
	#if length == 9:
	#	return len(set(str(number))) == length and len(str(number)) == length and not('0' in str(number))
	if length == 8:
		return len(set(str(number))) == length and len(str(number)) == length and not('0' in str(number)) and not('9' in str(number))
	if length == 7:
		return len(set(str(number))) == length and len(str(number)) == length and not('0' in str(number)) and not('9' in str(number)) and not('8' in str(number))
	if length == 6:
		return len(set(str(number))) == length and len(str(number)) == length and not('0' in str(number)) and not('9' in str(number)) and not('8' in str(number)) and not('7' in str(number))
	if length == 5:
		return len(set(str(number))) == length and len(str(number)) == length and not('0' in str(number)) and not('9' in str(number)) and not('8' in str(number)) and not('7' in str(number))  and not('6' in str(number)) 
	if length == 4:
		return len(set(str(number))) == length and len(str(number)) == length and '1' in str(number) and '2' in str(number) and '3' in str(number) and '4' in str(number)
	if length == 3:
		return len(set(str(number))) == length and len(str(number)) == length and '1' in str(number) and '2' in str(number) and '3' in str(number)
	if length == 2:
		return len(set(str(number))) == length and len(str(number)) == length and '1' in str(number) and '2' in str(number)
	return False

def isPrime(number):
	if number <= 1:
		return False
	elif number <=3:
        	return True
	elif number%2 == 0 or number%3 == 0:
		return False
	i = 5
	while i * i <= number:
		if number%i == 0 or number%(i + 2) == 0:
			return False
		i += 6
	return True

def checkPrimeFactors(number):
	if number in primes:
		return 1, [number]
	else:
		primefactors =[]
		for i in primes:
			while number%i==0 and number > 0:
				number /= i
				primefactors.append(i)
			if number==1:
				return len(set(primefactors)), primefactors

def nCr(n,r):
    f = math.factorial
    return int(f(n) / f(r) / f(n-r))