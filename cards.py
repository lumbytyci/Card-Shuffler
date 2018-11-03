
'''
Simple script containing information about cards and a deck of them.
There are 4 symbols or so called colors ["heart", "diamond", "spade", "club"],
for each card value so 4x13 cards in total not including jokers.
'''


# List of all possible symbols
symbols = ["heart", "diamond", "spade", "club"]

class Card:
    def __init__(self, value, symbol):
        self.value = value
        self.symbol = symbol


def generate_deck():
    deck = []
    for value in (list(range(1, 11)) + ["J", "Q", "K"]):
        for symbol in symbols:
            deck.append(Card(value, symbol))

    return deck
    # The pythonic way 
    # return [Card(value, color) for value in range(1, 14) for color in colors]

# for card in generate_deck(): PRINT THE DECK
#     print(card.value, "of", card.symbol + "s")