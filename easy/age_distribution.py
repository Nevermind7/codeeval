import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    age = int(test.strip())
    if age < 0 or age > 100:
        print('This program is for humans')
    elif 1 <= age <= 2:
        print('Still in Mama\'s arms')
    elif 3 <= age <= 4:
        print('Preschool Maniac')
    elif 5 <= age <= 11:
        print('Elementary school')
    elif 12 <= age <= 14:
        print('Middle school')
    elif 15 <= age <= 18:
        print('High school')
    elif 19 <= age <= 22:
        print('College')
    elif 23 <= age <= 65:
        print('Working for the man')
    elif 65 <= age <= 100:
        print('The Golden Years')
test_cases.close()
