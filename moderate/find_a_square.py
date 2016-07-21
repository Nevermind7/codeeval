import sys
from itertools import combinations
from math import sqrt
        
def distance(point, other):
    return sqrt((point[0]-other[0])**2 + (point[1]-other[1])**2)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    points = [x.replace('(', '').replace(')', '') for x in test.strip().split(', ')]
    points = [(int(point.split(',')[0]), int(point.split(',')[1])) 
              for point in points]
    combos = combinations(points, 2)
    distances = [distance(x, y) for (x,y) in combos]
    reduced = list(set(distances))
    if len(reduced) != 2:
        print('false')
    else:
        print('true')
test_cases.close()