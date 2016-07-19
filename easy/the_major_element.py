import sys
from collections import Counter

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    nums = [int(x) for x in test.strip().split(',')]
    half = int(len(nums)/2)
    c = Counter(nums)
    for num in nums:
        if c[num] > half:
            print(num)
            break
    else:
        print('None')
test_cases.close()
