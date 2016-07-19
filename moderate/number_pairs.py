import sys
from itertools import combinations

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    numbers, target = test.strip().split(';')
    numbers = [int(x) for x in numbers.split(',')]
    pairs = [(x,y) for (x,y) in combinations(numbers, 2) if x+y == int(target)]
    pairs = ['{},{}'.format(x, y) for (x,y) in pairs]
    print(';'.join(pairs) if pairs else 'NULL')
test_cases.close()
