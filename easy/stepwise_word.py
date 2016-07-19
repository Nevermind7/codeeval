import sys

def find_longest(words):
    long_first = sorted(words, key=lambda t: len(t))
    return long_first[0]
    
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    words = test.strip().split()
    word = find_longest(words)
    print(' '.join(['*'*i+char for i, char in enumerate(word)]))
        

test_cases.close()
