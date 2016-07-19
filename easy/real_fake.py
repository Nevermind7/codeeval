import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip().replace(' ', '')
    doubled = sum([int(x)*2 for x in test[::2]])
    checksum = doubled + sum([int(x) for x in test[1::2]])
    if checksum % 10 == 0:
        print('Real')
    else:
        print('Fake')
test_cases.close()
