import sys
import re

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        word, to_match = test.strip().split(',')
        if '*' not in to_match:
            if to_match in word:
                print('true')
            else:
                print('false')
        elif '*' in to_match:
            if '\*' in to_match:
                if to_match.replace('\*', '*') in word:
                    print('true')
                else:
                    print('false')
            else:
                if re.search(to_match.replace('*', '(.*)'), word):
                    print('true')
                else:
                    print('false')
