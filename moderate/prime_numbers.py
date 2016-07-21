import sys
from math import sqrt

def find_primes(num, primes):
    for number in range(max(primes)+1, num):
        for div in range(2, int(sqrt(number)+1)):
            if number % div == 0:
                break
        else:
            primes.append(number)
    return primes

test_cases = open(sys.argv[1], 'r')
primes = [2]
for test in test_cases:
    num = int(test.strip())
    if max(primes) > num:
        print(','.join([str(x) for x in primes if x < num]))
        continue
    print(','.join([str(x) for x in find_primes(num, primes)]))
test_cases.close()
