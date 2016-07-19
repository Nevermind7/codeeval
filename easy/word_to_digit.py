import sys

trans = {'zero': 0,
         'one': 1,
         'two': 2,
         'three': 3,
         'four': 4,
         'five': 5,
         'six': 6,
         'seven': 7,
         'eight': 8,
         'nine': 9}

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    words = test.strip().split(';')
    print(''.join([str(trans[x]) for x in words]))
test_cases.close()
