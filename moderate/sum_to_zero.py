import sys
from itertools import combinations

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    nums = [int(x) for x in test.strip().split(',')]
    c = combinations(nums, 4)
    print(len([x for x in c if sum(x) == 0]))
test_cases.close()
