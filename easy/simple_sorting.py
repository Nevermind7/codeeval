import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    nums = sorted([float(x) for x in test.strip().split()])
    print(' '.join(['{:.3f}'.format(num) for num in nums]))

test_cases.close()
