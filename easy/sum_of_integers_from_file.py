import sys

test_cases = open(sys.argv[1], 'r')
print(sum([int(test) for test in test_cases]))
test_cases.close()
