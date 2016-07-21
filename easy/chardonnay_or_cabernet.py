import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        possible = []
        wines, letters = test.strip().split(' | ')
        wines = wines.split()
        for wine in wines:
            wine_copy = wine
            match = True
            for letter in letters:
                if letter not in wine_copy:
                    match = False
                    break
                else:
                    wine_copy = wine_copy.replace(letter, '', 1)
            if match:
                possible.append(wine)
        if possible:
            print(' '.join(possible))
        else:
            print('False')
