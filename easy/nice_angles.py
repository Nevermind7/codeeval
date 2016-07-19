import sys

def to_degrees(decimal):
    hours = int(decimal)
    minutes = int((decimal-hours)*60)
    seconds = (decimal-hours-(minutes/60))*3600
    return hours, int(minutes), int(seconds)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    decimal = float(test.strip())
    degree = to_degrees(decimal)
    print('{}.{:02}\'{:02}\"'.format(*degree))
test_cases.close()
