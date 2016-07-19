import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    words, hints = [x.split() for x in test.strip().split(';')]
    hints = [int(x) -1 for x in hints]
    length = range(len(words))
    last_word_index = [i for i in length if i not in hints]
    sentence = dict(zip(hints+last_word_index, words))
    print(' '.join([sentence[i] for i in length]))

test_cases.close()
