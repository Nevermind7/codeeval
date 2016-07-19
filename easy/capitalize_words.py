import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    words = test.strip().split()
    words = [word[0].upper()+word[1:] for word in words]
    print(' '.join(words))
test_cases.close()
