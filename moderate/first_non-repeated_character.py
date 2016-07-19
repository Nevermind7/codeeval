import sys
from collections import Counter

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    word = test.strip()
    c = Counter(word)
    for char in word:
        if c[char] == 1:
            print(char)
            break
test_cases.close()
