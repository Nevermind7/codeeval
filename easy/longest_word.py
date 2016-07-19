import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    words = test.strip().split()
    lengths = [len(word) for word in words]
    print(words[lengths.index(max(lengths))])
test_cases.close()
