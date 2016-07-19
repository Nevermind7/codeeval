import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    elems = test.strip().split(',')
    words, nums = [], []
    for elem in elems:
        try:
            _ = int(elem)
            nums.append(elem)
        except ValueError:
            words.append(elem)
    words = ','.join([str(x) for x in words])
    nums = ','.join([str(x) for x in nums])
    if words and nums:
        print('{}|{}'.format(words, nums))
    else:
        print(words if words else nums)
test_cases.close()
