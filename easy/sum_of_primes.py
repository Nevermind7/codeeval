from math import sqrt

def isprime(num):
    for div in range(2, int(sqrt(num)+1)):
        if int(num/div) == num/div:
            return False
            break
    else:
        return True
        
SUM = 2
PRIMES = 1
NUM = 3

while PRIMES < 1000:
    if isprime(NUM):
        SUM += NUM
        PRIMES += 1
    NUM += 1

print(SUM)
    
