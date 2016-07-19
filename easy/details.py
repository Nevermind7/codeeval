import sys
import re

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    lines = [x for x in test.strip().split(',')]
    distances = []
    for line in lines:
        match = re.search('X\.*Y', line)
        length = match.span()[1] - match.span()[0] - 2
        distances.append(length)
    print(min(distances))

test_cases.close()
