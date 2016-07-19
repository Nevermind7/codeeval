import sys
import re
from math import sqrt

def dist(P1, P2):
    return int(sqrt(abs(P1[0]-P2[0])**2 + abs(P1[1]-P2[1])**2))

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    P1, P2 = test.strip().split(') (')
    P1 = [int(x) for x in re.sub('[(),]', '', P1).split()]
    P2 = [int(x) for x in re.sub('[(),]', '', P2).split()]
    print(dist(P1, P2))
test_cases.close()
