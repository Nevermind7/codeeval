import sys
from collections import Counter

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    nums = [int(x) for x in test.strip().split()]
    c = Counter([int(x) for x in nums])
    winner = min([num for num in c if c[num] == 1]) or None
    if winner:
        print(nums.index(winner)+1)
    else:
        print(0)
test_cases.close()
