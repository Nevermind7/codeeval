import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    rows = [x.split() for x in test.strip().split(' | ')]
    rows = [[int(x) for x in row] for row in rows]
    max_scores = []
    for i in range(len(rows[0])):
        col = [row[i] for row in rows]
        max_scores.append(str(max(col)))
    print(' '.join(max_scores))

test_cases.close()
