import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    num = test.strip()
    print(int(num) == sum([int(x)**len(num) for x in num]))
test_cases.close()
