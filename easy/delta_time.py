import sys
from datetime import datetime as dt

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    time1, time2 = test.strip().split()
    time1 = dt.strptime(time1, '%H:%M:%S')
    time2 = dt.strptime(time2, '%H:%M:%S')
    if time2 > time1:
        delta = time2 - time1
    else:
        delta = time1 - time2
    s = delta.seconds
    print('{:02}:{:02}:{:02}'.format(int(s/3600), int(s%3600/60), int(s%60)))
test_cases.close()
