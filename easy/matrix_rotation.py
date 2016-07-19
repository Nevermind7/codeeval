import sys
from math import sqrt

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    matrix = [x for x in test.strip().split()]
    dim = int(sqrt(len(matrix)))
    rot_matrix = []
    for i, row in enumerate(range(dim)):
        rot_matrix.extend(list(reversed(matrix[i::dim])))
    print(' '.join(rot_matrix))
test_cases.close()
