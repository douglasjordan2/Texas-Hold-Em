class Round:
  def __init__(self, id):
    self.id = id
    self.pot = 0
    self.board = None
    self.winner = None

  def add_bets(self, bets):
    self.pot += bets