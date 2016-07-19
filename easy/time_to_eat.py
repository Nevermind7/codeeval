import sys
from datetime import datetime as dt

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    times = test.strip().split()
    times = [dt.strptime(time, '%H:%M:%S') for time in times]
    times = [dt.strftime(x, '%H:%M:%S') for x in reversed(sorted(times))]
    print(' '.join(times))
test_cases.close()
