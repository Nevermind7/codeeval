import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        virus, antivir = test.split(' | ')
        sum_virus = sum([int(x, base=16) for x in virus.split()])
        sum_antivir = sum([int(x, base=2) for x in antivir.split()])
        if sum_antivir >= sum_virus:
            print('True')
        else:
            print('False')
