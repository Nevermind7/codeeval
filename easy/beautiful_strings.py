import sys
from collections import Counter, OrderedDict
import re

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip().lower()
    test = re.sub('[^a-z]', '', test)
    c = OrderedDict(reversed(sorted(Counter(test).items(), key=lambda t: t[1])))
    print(sum([x*y for (x,y) in zip(c.values(), reversed(range(27)))]))
test_cases.close()
