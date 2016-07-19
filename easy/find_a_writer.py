import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    coded, keys = test.strip().split('|')
    keys = [int(key) for key in keys.split()]
    print(''.join([coded[key-1]for key in keys]))
test_cases.close()
