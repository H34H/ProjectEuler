import datetime
import math
import sys
import itertools
from array import array

t = datetime.datetime.now()



def get_sieve(bound):
    a = array('B', (1 for i in range(bound + 1)))
    a[0] = 0
    a[1] = 0
    for i in range(2, int(math.sqrt(bound)) + 1):
        if a[i]:
            for j in range(i * i, bound + 1, i):
                a[j] = 0
    return a


def gen_primes_from_sieve(sieve):
    for i in range(2, len(sieve)):
        if sieve[i]:
            yield i

def get_primes(n):
    n -= 1 # below n, so the inclusive bound is n - 1 (only matter for n prime)                                                             
    return (gen_primes_from_sieve(get_sieve(n))) if n >= 2 else 0

runtime  = datetime.datetime.now() - t
print (runtime)

###