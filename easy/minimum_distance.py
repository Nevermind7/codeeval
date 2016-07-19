import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    items = test.strip().split()
    houses = [int(x) for x in items[1:]]
    distances = []
    for house in range(max(houses)+1):
        distances.append(sum([abs(house-home) for home in houses]))
    print(min(distances))
test_cases.close()
