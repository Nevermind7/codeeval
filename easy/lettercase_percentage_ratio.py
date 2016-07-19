import sys
from string import ascii_uppercase as upper, ascii_lowercase as lower

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    chars = [x for x in test.strip()]
    small = [x for x in chars if x in lower]
    big = [x for x in chars if x in upper]
    print('lowercase: {:.2f} uppercase: {:.2f}'.format(100*len(small)/len(chars), 
                                                       100*len(big)/len(chars)))

test_cases.close()
