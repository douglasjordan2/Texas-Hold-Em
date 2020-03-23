import time
import os

clear = lambda : os.system('tput reset')

from game import Game
from round import Round
from board import Board
from deck import Deck
from players import Player

clear()
print("")
name = input('Enter your name: ')
# name = "You"

player = Player(name, 1000)
dealer = Player('Dealer', 1000)

time.sleep(0.5)
clear()
print("")
print(f"Welcome to Texas Hold Em, {player}!")
print("")

# initiate game
players = [dealer, player]
game = Game(players)

# counter to keep track of rounds
counter = 0

# game loops until there is a winner
while game.winner is None:
  # initiate new deck, board before each round
  deck = Deck()
  board = Board()

  # initiate new round
  round_id = f'Round {counter + 1}'
  round = Round(round_id)
  
  # populate dealer's hole cards
  for i in range(2):
    card = deck.draw()
    dealer.add_card(card)

  # populate player's hole cards
  for i in range(2):
    card = deck.draw()
    player.add_card(card)

  # show board and game info
  time.sleep(1)
  clear()
  print(f'Your Credits: {player.credits} | Dealer Credits: {dealer.credits}')
  print("")
  print("")
  print(f"\tDealer: [] []")
  print("")
  print("\tX [] [] [] [] [] ")
  print("")
  print(f'\t{player}: {player.hand[0]} {player.hand[1]}')
  print("")
  print("")

  # first bets
  player_bet = input('Make your bet: ')

  # burn one
  card = deck.draw()
  board.burn(card)
  
  # flop
  for i in range(3):
    card = deck.draw()
    board.turn(card)

  # update board
  time.sleep(1)
  clear()
  print(f'Your Credits: {player.credits} | Dealer Credits: {dealer.credits}')
  print("")
  print("")
  print(f"\tDealer: [] []")
  print("")
  print(f"Flop:   X {board.board[0]} {board.board[1]} {board.board[2]} [] [] ")
  print("")
  print(f'\t{player}: {player.hand[0]} {player.hand[1]}')
  print("")
  print("")

  # analyze player's hand and bet
  print(f'{player.analyze(board.board)}')
  player_bet = input('Make your bet: ')

  # turn
  card = deck.draw()
  board.burn(card)
  card = deck.draw()
  board.turn(card)

  # update board
  time.sleep(1)
  clear()
  print(f'Your Credits: {player.credits} | Dealer Credits: {dealer.credits}')
  print("")
  print("")
  print(f"\tDealer: [] []")
  print("")
  print(f"Turn:   X {board.board[0]} {board.board[1]} {board.board[2]} {board.board[3]} [] ")
  print("")
  print(f'\t{player}: {player.hand[0]} {player.hand[1]}')
  print("")
  print("")

  # analyze player's hand and bet
  print(f'{player.analyze(board.board)}')
  player_bet = input('Make your bet: ')

  # river
  card = deck.draw()
  board.burn(card)
  card = deck.draw()
  board.turn(card)

  # update board
  time.sleep(1)
  clear()
  print(f'Your Credits: {player.credits} | Dealer Credits: {dealer.credits}')
  print("")
  print("")
  print(f"\tDealer: [] []")
  print("")
  print(f"River:  X {board.board[0]} {board.board[1]} {board.board[2]} {board.board[3]} {board.board[4]} ")
  print("")
  print(f'\t{player}: {player.hand[0]} {player.hand[1]}')
  print("")
  print("")
  
  # analyze player's hand and bet
  print(f'Your hand analysis: {player.analyze(board.board)}')
  player_bet = input('Make your bet: ')

  player.analyze(board.board)
  dealer.analyze(board.board)

  clear()
  print(f"Player: {player.best_hand} | Dealer: {dealer.best_hand}")
  if player.best_hand > dealer.best_hand:
    round.winner = player
  elif dealer.best_hand > player.best_hand:
    round.winner = dealer
  else:
    p = player.tie_breaker.sort
    d = dealer.tie_breaker.sort

    if p > d:
      round.winner = player
    elif d > p:
      round.winner = dealer
    else:
      p = player.kicker.sort
      d = dealer.kicker.sort

      if p > d:
        round.winner = player
      elif d > p:
        round.winner = dealer
      else:
        round.winner = 'Split Pot'

  print("")
  print("Player:", [f'{card.rank}{card.suit}' for card in player.hand + board.board])
  print("")
  print("Dealer:", [f'{card.rank}{card.suit}' for card in dealer.hand + board.board])
  print("")

  game.add_round(round)

  for round in game.rounds:
    print(f'{round.id} Winner: {round.winner}')

  print("")
  input('Press Enter to Continue.')

  player.reset()
  dealer.reset()

  counter += 1


# TODO
## finish betting stuff - remove bets from credits, add bets to round pot, award pot to winner
## learn and implement poker hand odds
## analyze dealer's hand and make him bet accordingly
## provide game summary when someone wins - biggest pot, hands played, best hand
## refactor into django - make endpoints, push data to FE
## build FE app

  