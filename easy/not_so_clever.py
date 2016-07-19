import sys

def stupid_sort(to_sort, num):
    for _ in range(num):
        for i, elem in enumerate(to_sort[:-1]):
            if elem > to_sort[i+1]:
                to_sort[i], to_sort[i+1] = to_sort[i+1], to_sort[i]
                break
    return to_sort

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    to_sort, num = test.strip().split(' | ')
    num = int(num)
    to_sort = [int(x) for x in to_sort.split()]
    stupidly_sorted = stupid_sort(to_sort, num)
    print(' '.join([str(x) for x in stupidly_sorted]))
test_cases.close()
