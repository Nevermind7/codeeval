import sys

def divisible(num, div):
    if int(num/div) == num/div:
        return True
    else:
        return False

test_cases = open(sys.argv[1],'r')        
for test in test_cases:
    if not test:
        continue
    output = ''
    div1, div2, end = (int(x) for x in test.split())
    for num in range(1, end+1):
        if divisible(num, div1):
            if divisible(num, div2):
                output += 'FB '
            else:
                output+= 'F '
        elif divisible(num, div2):    
            output += 'B '
        else:
            output += '{} '.format(num)
    print(output)
test_cases.close()
