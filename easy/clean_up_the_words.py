import sys
import re

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip().lower()
    found = [x for x in re.findall('[a-z]*', test) if x]
    print(' '.join(found))
test_cases.close()
