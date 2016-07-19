import sys

def swap_first_last(word):
    return word[-1] + word[1:-1] + word[0]
    
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    words = test.strip().split()
    words = [swap_first_last(word) for word in words]
    print(' '.join(words))
test_cases.close()
