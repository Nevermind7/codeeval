import sys

board = [[0 for x in range(256)] for x in range(256)]

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    instruction = test.strip().split()
    if len(instruction) == 2:
        pos = instruction[1]
    elif len(instruction) == 3:
        pos, val = instruction[1:]
    if instruction[0] == 'SetRow':
        board[int(pos)] = [int(val) for x in range(256)]
    elif instruction[0] == 'SetCol':
        for index, row in enumerate(board):
            board[index][int(pos)] = int(val)
    elif instruction[0] == 'QueryRow':
        print(sum(board[int(pos)]))
    elif instruction[0] == 'QueryCol':
        print(sum([board[index][int(pos)] for index, row in enumerate(board)]))
test_cases.close()
