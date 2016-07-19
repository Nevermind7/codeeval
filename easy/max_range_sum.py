import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    days, move = [x for x in test.strip().split(';')]
    days = int(days)
    moves = [int(x) for x in move.split()]
    streaks = [moves[x:x+days] for x in range(len(moves)-days+1)]
    gains = max([sum(x) for x in streaks])
    print(gains if gains >= 0 else 0)
test_cases.close()
