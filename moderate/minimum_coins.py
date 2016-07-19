import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    rest = int(test.strip())
    fives = int(rest / 5)
    rest = rest - fives * 5
    threes = int(rest / 3)
    rest = rest - threes * 3
    print(fives + threes + rest)
test_cases.close()
