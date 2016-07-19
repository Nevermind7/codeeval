import sys
from collections import OrderedDict

vals = {'ONE HUNDRED': 10000,
        'FIFTY': 5000,
        'TWENTY': 2000,
        'TEN': 1000,
        'FIVE': 500,
        'TWO': 200,
        'ONE': 100,
        'HALF DOLLAR': 50,
        'QUARTER': 25,
        'DIME': 10,
        'NICKEL': 5,
        'PENNY': 1}
CASH = OrderedDict(reversed(sorted(vals.items(), key=lambda t: t[1])))

def calc_return(to_pay, given):
    ret = []
    rest = given - to_pay
    for val in CASH:
        amount = int(rest / CASH[val])
        if amount:
            rest -= CASH[val] * amount
            for _ in range(amount):
                ret.append(val)
    return(','.join([str(x) for x in ret]))

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    to_pay, given = [int(float(x)*100) for x in test.strip().split(';')]
    if to_pay == given:
        print('ZERO')
        continue
    elif to_pay > given:
        print('ERROR')
        continue
    else:
        print(calc_return(to_pay, given))

test_cases.close()
