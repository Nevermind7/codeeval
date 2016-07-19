import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    num, bit1, bit2 = (int(x.strip()) for x in test.split(','))
    binary = bin(num).replace('0b', '')
    print(str(binary[-bit1] == binary[-bit2]).lower())

test_cases.close()
