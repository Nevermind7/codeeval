import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    text, to_scrub = test.strip().split(', ')
    for char in to_scrub:
        text = text.replace(char, '')
    print(text)

test_cases.close()
