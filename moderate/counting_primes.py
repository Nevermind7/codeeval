import sys
from math import sqrt

def primes_between(start, end):
    primes = 0
    for num in range(start, end+1):
        for div in range(2, int(sqrt(num))+1):
            if num % div == 0:
                break
        else:
            primes += 1
    return primes

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    start, end = [int(x) for x in test.strip().split(',')]
    print(primes_between(start, end))
test_cases.close()
