import sys

def deduplicate(word):
    new_word = []
    for i, char in enumerate(word):
        if i == 0:
            curr = char
            new_word.append(char)
            continue
        else:
            if char == curr:
                continue
            else:
                curr = char
                new_word.append(char)
    return ''.join(new_word)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    words = [deduplicate(x) for x in test.strip().split()]
    print(' '.join(words))
test_cases.close()
