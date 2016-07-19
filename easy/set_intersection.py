import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    set1, set2 = [set(x.split(',')) for x in test.strip().split(';')]
    print(','.join([str(x) for x in sorted(set1 & set2)]) or '')
test_cases.close()
