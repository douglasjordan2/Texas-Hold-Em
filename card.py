class Card:
  def __init__(self, rank, suit, sort, next):
    self.rank = rank
    self.suit = suit
    self.sort = sort
    self.next = next
  
  def __str__(self):
    return f'{self.rank}{self.suit}'