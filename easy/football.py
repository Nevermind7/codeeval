import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    fandom = {}
    countries = test.strip().split(' | ')
    for i, country in enumerate(countries):
        for team in sorted(country.split()):
            if int(team) not in fandom:
                fandom[int(team)] = [str(i+1)]
            else:
                fandom[int(team)].append(str(i+1))
    output = ''
    for key in sorted(fandom.keys()):
        output += '{}:{}; '.format(key, ','.join(fandom[key]))
    print(output.strip())
test_cases.close()
