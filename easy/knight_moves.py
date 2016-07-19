import sys
from itertools import product

cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
rows = ['1', '2', '3', '4', '5', '6', '7', '8']
board = [x+y for (x,y) in product(cols, rows)]

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    pos = test.strip()
    col, row = cols.index(pos[0]), rows.index(pos[1])
    moves = []
    #top
    if row < 6:
        if col < 7:
            moves.append(cols[col+1]+rows[row+2])
        if col > 0:
            moves.append(cols[col-1]+rows[row+2])
    #right
    if col < 6:
        if row < 7:
            moves.append(cols[col+2]+rows[row+1])
        if row > 0:
            moves.append(cols[col+2]+rows[row-1])
    #bottom
    if row > 1:
        if col < 7:
            moves.append(cols[col+1]+rows[row-2])
        if col > 0:
            moves.append(cols[col-1]+rows[row-2])
    #left
    if col > 1:
        if row < 7:
            moves.append(cols[col-2]+rows[row+1])
        if row > 0:
            moves.append(cols[col-2]+rows[row-1])
    print(' '.join(list(sorted(moves))))
test_cases.close()
