import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    x, n = (int(item) for item in test.split(','))
    for num in range(x):
        if n*num >= x:
            print(n*num)
            break
test_cases.close()
