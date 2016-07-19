import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    nums = [int(x) for x in test.strip().split()]
    diffs = []
    for i, elem in enumerate(nums[:-1]):
        diffs.append(abs(nums[i]-nums[i+1]))
    for diff in range(1, len(nums)-1):
        if diff not in diffs:
            print('Not jolly')
            break
    else:
        print('Jolly')
test_cases.close()
