import random
from card import Card

class Deck:
  def __init__(self):
    self.suits = ['H', 'S', 'C', 'D']
    self.ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    self.deck = []

    for s in self.suits:
      for r in range(len(self.ranks)):
        next = self.ranks[r + 1] if r is not len(self.ranks) - 1 else self.ranks[0]
        card = Card(self.ranks[r], s, r + 1, next)
        self.deck.append(card)

    random.shuffle(self.deck)

  def draw(self):
    card = self.deck.pop()
    return card