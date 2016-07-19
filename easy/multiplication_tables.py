tables = [[x*y for x in range(1,13)] for y in range(1,13)]

for table in tables:
    print(''.join([str(x).rjust(4) for x in table]).lstrip())
