import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    elems, swapping = test.strip().split(':')
    elems = [int(x) for x in elems.strip().split()]
    swapping = [x for x in swapping.split(',')]
    for swap in swapping:
        swap1, swap2 = [int(x) for x in swap.split('-')]
        elems[swap1], elems[swap2] = elems[swap2], elems[swap1]
    print(' '.join([str(x) for x in elems]))
test_cases.close()
