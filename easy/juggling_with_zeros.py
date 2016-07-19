import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    seq = [x for x in test.strip().split()]
    instr = list(zip(seq[::2], seq[1::2]))
    binary = ''
    for item in instr:
        flag, num = item
        if flag == '00':
            binary += ''.join(['1' for _ in num])
        elif flag == '0':
            binary += num
    print(int(binary, 2))
test_cases.close()
