import sys

to_digit = list('abcdefghij')
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    hidden = list(test.strip())
    found = []
    for char in hidden:
        try:
            _ = int(char)
            found.append(str(char))
        except ValueError:
            if char in to_digit:
                found.append(str(to_digit.index(char)))
    if found:
        print(''.join(found))
    else:
        print('NONE')
test_cases.close()
