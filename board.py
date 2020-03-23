class Board:
  def __init__(self):
    self.discard = []
    self.board = []

  def burn(self, card):
    self.discard.append(card)

  def turn(self, card):
    self.board.append(card)