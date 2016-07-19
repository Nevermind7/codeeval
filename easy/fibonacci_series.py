import sys

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print(fib(int(test)))
test_cases.close()
