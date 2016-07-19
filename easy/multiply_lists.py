import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    nums1, nums2 = test.strip().split('|')
    nums1 = [int(x) for x in nums1.split()]
    nums2 = [int(x) for x in nums2.split()]
    prod = [x*y for (x,y) in zip(nums1, nums2)]
    print(' '.join([str(x) for x in prod]))
test_cases.close()
