import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    num = int(test.strip())
    print(bin(num).replace('0b', ''))

test_cases.close()
