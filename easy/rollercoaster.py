import sys
from string import ascii_uppercase as upper, ascii_lowercase as lower

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    sentence = list(test.strip())
    sentence[0] = sentence[0].upper()
    nxt = 'low'
    for i, char in enumerate(sentence):
        if i == 0:
            continue
        if char in upper+lower:
            if nxt == 'low':
                sentence[i] = sentence[i].lower()
                nxt = 'up'
            elif nxt == 'up':
                sentence[i] = sentence[i].upper()
                nxt = 'low'
    print(''.join(sentence))
test_cases.close()
