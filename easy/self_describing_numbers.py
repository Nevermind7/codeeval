import sys
from collections import Counter

def is_self_descr(num):
    c = Counter(num)
    for index, digit in enumerate(num):
        if int(digit) != c[str(index)]:
            return '0'
            break
    else:
        return '1'
    
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print(is_self_descr(test.strip()))
test_cases.close()
