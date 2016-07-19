import sys
import json

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    items = json.loads(test.strip())['menu']['items']
    items = [item for item in items if item]
    print(sum([item['id'] for item in items if 'label' in item]))
test_cases.close()
