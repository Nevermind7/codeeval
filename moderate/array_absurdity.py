import sys
from collections import Counter

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    _, nums = test.strip().split(';')
    nums = [int(x) for x in nums.split(',')]
    c = Counter(nums)
    for num in c:
        if c[num] == 2:
            print(num)
test_cases.close()
