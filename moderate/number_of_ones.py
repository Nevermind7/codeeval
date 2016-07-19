import sys
import re

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    num = int(test.strip())
    num_of_ones = len(re.findall('1', bin(num)))
    print(str(num_of_ones))
test_cases.close()
