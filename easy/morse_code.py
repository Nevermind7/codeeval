import sys

morse_alphabet ={
        "A" : ".-",
        "B" : "-...",
        "C" : "-.-.",
        "D" : "-..",
        "E" : ".",
        "F" : "..-.",
        "G" : "--.",
        "H" : "....",
        "I" : "..",
        "J" : ".---",
        "K" : "-.-",
        "L" : ".-..",
        "M" : "--",
        "N" : "-.",
        "O" : "---",
        "P" : ".--.",
        "Q" : "--.-",
        "R" : ".-.",
        "S" : "...",
        "T" : "-",
        "U" : "..-",
        "V" : "...-",
        "W" : ".--",
        "X" : "-..-",
        "Y" : "-.--",
        "Z" : "--..",
        "1" : ".----",
        "2" : "..---",
        "3" : "...--",
        "4" : "....-",
        "5" : ".....",
        "6" : "-....",
        "7" : "--...",
        "8" : "---..",
        "9" : "----.",
        "0" : "-----"}

inverse_morse_alphabet = dict((v,k) for (k,v) in morse_alphabet.items())

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        out = []
        test = test.strip().replace('  ', ',')
        words = test.split(',')
        for word in words:
            letters = word.split()
            translated = ''.join([inverse_morse_alphabet[letter] 
                                  for letter in letters])
            out.append(translated)
        print(' '.join(out))
