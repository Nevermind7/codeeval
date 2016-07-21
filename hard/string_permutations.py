import sys
from itertools import permutations

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        permutate = test.strip()
        combos = [''.join(list(x)) for x in permutations(permutate)]
        print(','.join(sorted([x for x in combos])))
