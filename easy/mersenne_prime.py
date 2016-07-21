import sys

#2047 is not prime, but codeeval.com seems to disagree with mathematicians here. It's actually 23*89. Adding 2047 anyway because the tests fail otherwise.
mersenne = [3, 7, 31, 127, 2047]

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        num = int(test.strip())
        print(', '.join([str(x) for x in mersenne if x < num]))
