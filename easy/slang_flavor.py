import sys
import re

phrases = [', yeah!', 
           ', this is crazy, I tell ya.', 
           ', can U believe this?', 
           ', eh?', 
           ', aw yea.', 
           ', yo.', 
           '? No way!',
           '. Awesome!']

def phrase_gen():
    while True:
        for phrase in iter(phrases):
            try:
                yield phrase
            except StopIteration:
                pass
            
def slang(word, phrase):
    return re.sub('[\.\!\?]', next(phrase), word)
           
test_cases = open(sys.argv[1], 'r')
phrase = phrase_gen()
slangify = False
for test in test_cases:
    words = test.strip().split()
    for i, word in enumerate(words):
        if re.search('[\.\!\?]', word) and slangify:
            words[i] = slang(word, phrase)
            slangify = False
        elif re.search('[\.\!\?]', word) and not slangify:
            slangify = True
            continue
    print(' '.join(words))
test_cases.close()


