import sys
from itertools import product

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        length, letters = test.strip().split(',')
        perms = [''.join(x) for x in 
                 product(letters, repeat=int(length))]
        print(','.join(sorted(list(set(perms)))))
