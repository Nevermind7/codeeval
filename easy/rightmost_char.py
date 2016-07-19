import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    word, char = [x.strip() for x in test.split(',')]
    if char not in word:
        print(-1)
        continue
    else:
        for index, c in enumerate(word[::-1]):
            if c == char:
                print(len(word)-index-1)
                break
test_cases.close()
