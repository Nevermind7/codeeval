import sys

test_cases = [test.strip() for test in open(sys.argv[1], 'r').readlines()]
num = int(test_cases[0])
lines = [x for x in reversed(sorted(test_cases[1:], key= lambda t: len(t)))]
for i in range(num):
    print(lines[i])
