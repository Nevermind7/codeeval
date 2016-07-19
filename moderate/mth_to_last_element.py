import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip().split()
    i = int(test[-1])
    try:
        print(test[-(i+1)])
    except IndexError:
        pass

test_cases.close()
