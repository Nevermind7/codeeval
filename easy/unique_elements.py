import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print(','.join([str(x) for x in sorted(list(set([int(x) for x in test.strip().split(',')])))]))
test_cases.close()
