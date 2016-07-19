import sys

def pascal_triangle(depth):
    triangle = [1]
    curr_row = triangle
    for _ in range(depth-1):
        curr_row = next_iteration(curr_row)
        for elem in curr_row:
            triangle.append(elem)
    return triangle

def next_iteration(row):
    row = [0] + row + [0]
    new_row = []
    for elem in range(len(row)-1):
        new_row.append(row[elem] + row[elem+1])
    return new_row

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    depth = int(test.strip())
    print(' '.join([str(x) for x in pascal_triangle(depth)]))
test_cases.close()
