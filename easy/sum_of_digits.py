import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    digits = [int(x) for x in test.strip()]
    print(sum(digits))
test_cases.close()
