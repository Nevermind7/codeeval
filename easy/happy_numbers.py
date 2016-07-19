import sys

def is_happy(num):
    chain = []
    while True:
        if num == 1:
            return '1'
        num = sum([int(x)**2 for x in str(num)])
        if num in chain:
            return '0'
        chain.append(num)
        
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    num = test.strip()
    print(is_happy(num))
test_cases.close()
