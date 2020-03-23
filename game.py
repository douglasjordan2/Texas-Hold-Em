class Game:
  def __init__(self, players):
    self.players = players
    self.rounds = []
    self.winner = None

  def add_round(self, round):
    self.rounds.append(round)