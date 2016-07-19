import sys
from string import ascii_lowercase as lower

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    text = test.strip().lower()
    missing = []
    for char in lower:
        if char not in text:
            missing.append(char)
    print(''.join(missing)or 'NULL')
test_cases.close()
