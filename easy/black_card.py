import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    players, num = test.strip().split(' | ')
    players = [x for x in players.split()]
    num = int(num)
    while len(players) > 1:
        if num < len(players):
            del players[num-1]
        else:
            del players[num%len(players)-1]
    print(players[0])
test_cases.close()
