import sys
import re

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    count, num = [int(x) for x in test.strip().split()]
    binaries = [bin(x).replace('0b', '') for x in range(1, int(num)+1)]
    filtered = [x for x in binaries if len(re.findall('0', x)) == count]
    print(len(filtered))
test_cases.close()
