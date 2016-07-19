import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    num, pattern = test.strip().split()
    if '+' in pattern:
        first, second = pattern.split('+')
        result = int(num[:len(first)] or num[0]) + int(num[-len(second):])
    elif '-' in pattern:
        first, second = pattern.split('-')
        result = int(num[:len(first)] or num[0]) - int(num[-len(second):])
    else:
        result = None
    print(result)
    

test_cases.close()
