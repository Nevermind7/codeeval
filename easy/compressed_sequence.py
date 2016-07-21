import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    nums = [x for x in test.strip().split()]
    curr_num = None
    counter = 1
    sequences = ''
    for num in nums:
        if not curr_num:
            curr_num = num
        else:
            if num == curr_num:
                counter += 1
            else:
                sequences += '{} {} '.format(counter, curr_num)
                curr_num = num
                counter = 1
    else:
        sequences += '{} {} '.format(counter, curr_num)
    print(sequences.strip())
test_cases.close()
