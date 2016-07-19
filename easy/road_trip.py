import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    cities = test.strip().split(';')[:-1]
    distances = sorted([int(city.split(',')[1]) for city in cities])
    rel_dist = []
    for index, dist in enumerate(distances):
        if index:
            rel_dist.append(dist-distances[index-1])
        else:
            rel_dist.append(dist)
    print(','.join([str(x) for x in rel_dist]))
test_cases.close()
