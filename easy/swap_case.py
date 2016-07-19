import sys

def change_cap(word):
    return ''.join([c.upper() if c==c.lower() else c.lower() for c in word])

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    words = test.strip().split()
    words = [change_cap(word) for word in words]
    print(' '.join(words))
test_cases.close()
