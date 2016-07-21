import sys

ancestors = {'30': ['30'],
             '8': ['30'],
             '52': ['30'],
             '3': ['8', '30'],
             '20': ['8', '30'],
             '10': ['20', '8', '30'],
             '29': ['20', '8', '30']}

def find_common_ancestor(num1, num2):
    if num1 in ancestors[num2]:
        return num1
    elif num2 in ancestors[num1]:
        return num2
    if len(ancestors[num1]) == len(ancestors[num2]):
        return ancestors[num1][0]
    elif len(ancestors[num1]) > len(ancestors[num2]):
        return ancestors[num2][0]
    elif len(ancestors[num1]) < len(ancestors[num2]):
        return ancestors[num1][0]


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    num1, num2 = test.strip().split()
    print(find_common_ancestor(num1, num2))
test_cases.close()
