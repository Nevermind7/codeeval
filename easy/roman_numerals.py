import sys

def numerals(base):
    """Roman numerals are different for every order of magnitude.
	   Returns the appropriate numerals for the OOM."""
    if base == 1:
        return ('I', 'V', 'X')
    elif base == 10:
        return ('X', 'L', 'C')
    elif base == 100:
        return ('C', 'D', 'M')
    elif base == 1000:
        return ('M', '', '')

def romanize(digit, base):
    """Returns the appropriate numeral representation for a given digit."""
    unit, half, decade = numerals(base)
    if 0 < digit < 4:
        return unit*digit
    elif digit == 4:
        return unit+half
    elif digit == 5:
        return half
    elif 5 < digit < 9:
        return half+unit*(digit-5)
    elif digit == 9:
        return unit+decade
    else:
        return ''

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    num = test.strip()
    romanized = ''
    for i, digit in enumerate(num):
        romanized += romanize(int(digit), int(10**len(num)/10**(i+1)))
    print(romanized)
test_cases.close()
