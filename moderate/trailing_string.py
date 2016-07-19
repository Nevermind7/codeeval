import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    text, end = test.strip().split(',')
    if text.endswith(end):
        print('1')
    else:
        print('0')
test_cases.close()
