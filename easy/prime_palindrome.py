from math import sqrt

def palindrome(num):
    return str(num) == str(num)[::-1]
    
def isprime(num):
    for div in range(2, int(sqrt(num))+1):
        if int(num/div) == num/div:
            return False
            break
    else:
        return True
        
for num in reversed(range(1001)):
    if isprime(num):
        if palindrome(num):
            print(num)
            break
