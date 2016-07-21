import sys

ranks = ['2', '3', '4', '5', '6', '7', '8', 
         '9', '10', 'J', 'Q', 'K', 'A']

class Card:
    def __init__(self, card, trump):
        self.suit = card[-1]
        self.rank = ranks.index(card[:-1])
        self.is_trump = self.suit == trump
    
    def draws_with(self, other):
        if not self.is_trump and not other.is_trump and self.rank == other.rank:
            return True
        else:
            return False
    
    def __str__(self):
        return '{}{}'.format(ranks[self.rank], self.suit)
        
    def beats(self, other):
        if self.is_trump and not other.is_trump:
            return str(self)
        elif not self.is_trump and not other.is_trump:
            if self.rank > other.rank:
                return str(self)
            else:
                return str(other)
        elif not self.is_trump and other.is_trump:
            return str(other)
        elif self.is_trump and other.is_trump:
            if self.rank > other.rank:
                return str(self)
            else:
                return str(other)

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        cards, trump = test.strip().split(' | ')
        first, second = cards. split()
        c1 = Card(first, trump)
        c2 = Card(second, trump)
        if c1.draws_with(c2):
            print(' '.join([str(c1), str(c2)]))
        else:
            print(c1.beats(c2))
