import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    num, div = [int(x) for x in test.strip().split(',')]
    print(num-(int(num/div)*div))

test_cases.close()
