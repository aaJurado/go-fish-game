
from random import shuffle


class Card:
    """A single standard playing card."""

    _FACE_NAMES = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}

    def __init__(self, value, suit):
        """Initialize a Card with a value (2–14) and a suit."""
        self.suit = suit
        self.value = value
        self.name = self._FACE_NAMES.get(value, str(value))

    def __str__(self):
        """Return a string like 'King of Spades'."""
        return f"{self.name} of {self.suit}"


class Deck:
    """A standard 52-card deck."""

    def __init__(self):
        """Create and shuffle a 52-card deck."""
        self.cards = []
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        for suit in suits:
            for value in range(2, 15):  # 2 through 14
                self.cards.append(Card(value, suit))
        shuffle(self.cards)

    def draw(self):
        """Remove and return the top card, or raise if empty."""
        if not self.cards:
            raise RuntimeError("Cannot draw from an empty deck.")
        return self.cards.pop()
