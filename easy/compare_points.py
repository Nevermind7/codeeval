import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    X1, Y1, X2, Y2 = [int(x) for x in test.strip().split()]
    dX, dY = X2-X1, Y2-Y1
    if dX == dY == 0:
        print('here')
    elif dX == 0:
        if dY > 0:
            print('N')
        else:
            print('S')
    elif dY == 0:
        if dX > 0:
            print('E')
        else:
            print('W')
    elif dX > 0 and dY < 0:
        print('SE')
    elif dX > 0 and dY > 0:
        print('NE')
    elif dX < 0 and dY < 0:
        print('SW')
    elif dX < 0 and dY > 0:
        print('NW')
test_cases.close()
