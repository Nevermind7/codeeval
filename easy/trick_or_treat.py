import sys

MULTIPLIER = {'Vampires': 3,
              'Zombies': 4,
              'Witches': 5}

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    items = test.strip().split(', ')
    vamps, zombs, witches, houses = [int(x.split(': ')[1]) for x in items]
    kids = sum([vamps, zombs, witches])
    candy = sum([vamps*MULTIPLIER['Vampires']*houses,
                 zombs*MULTIPLIER['Zombies']*houses,
                 witches*MULTIPLIER['Witches']*houses])
    print(int(candy/kids))
test_cases.close()
