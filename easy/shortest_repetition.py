import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    for length in range(1, len(test)+1):
        if len(test) % length == 0:
            if test[:length]*(int(len(test)/length)) == test:
                print(length)
                break
test_cases.close()
