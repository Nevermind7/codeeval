import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    bugged, final = test.replace('\n', '').split(' | ')
    bugs = 0
    for i, char in enumerate(bugged):
        if char != final[i]:
            bugs +=1
    if not bugs:
        print('Done')
    elif bugs < 3:
        print('Low')
    elif bugs < 5:
        print('Medium')
    elif bugs < 7:
        print('High')
    else:
        print('Critical')

test_cases.close()
