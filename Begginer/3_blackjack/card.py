# The Card class - one single playing card.
# Each card has a suit (like hearts) and a rank (like King, worth 10).

class Card:
    def __init__(self, suit, rank):
        self.suit = suit  # e.g. "♥"
        self.rank = rank  # a dictionary like {"rank": "K", "value": 10}

    # __str__ decides what shows up when we print a card
    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"
