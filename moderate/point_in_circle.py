import sys

def get_XY(point):
    point = point.replace('(', '')
    point = point.replace(')', '')
    x, y = [float(x) for x in point.split(', ')]
    return x, y

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip().split('; ')
    centerX, centerY = get_XY(test[0].split(': ')[1])
    radius = float(test[1].split(': ')[1])
    pointX, pointY = get_XY(test[2].split(': ')[1])
    is_inside = (centerX - pointX)**2 + (centerY - pointY)**2 < radius**2
    print(str(is_inside).lower())
test_cases.close()
