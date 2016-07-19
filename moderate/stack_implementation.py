import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    items = [x for x in reversed(test.strip().split())]
    print(' '.join(items[::2]))

test_cases.close()
