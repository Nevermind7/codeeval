import sys
import re

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    right = len(re.findall('(?=(>>-->))', test))
    left = len(re.findall('(?=(<--<<))', test))
    print(left+right)
test_cases.close()
