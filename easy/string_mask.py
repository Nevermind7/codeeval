import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    word, code = test.strip().split()
    paired = zip(word, code)
    encoded = ''.join([x.upper() if y == '1' else x for (x, y) in paired])
    print(encoded)
test_cases.close()
