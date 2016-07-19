import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    people, death = [int(x) for x in test.strip().split(',')]
    living = {x: 1 for x in range(people)}
    obituary = []
    counter = 0
    while any([living[x] for x in living]):
        for x in range(people):
            if living[x]:
                counter += 1
                if counter == death:
                    obituary.append(x)
                    living[x] = 0
                    counter = 0
    print(' '.join([str(x) for x in obituary]))
test_cases.close()
