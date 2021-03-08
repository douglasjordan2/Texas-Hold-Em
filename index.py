import time
import os

#small change to check gh configuration

clear = lambda : os.system("tput reset")

from game import Game
from round import Round
from board import Board
from deck import Deck
from players import Player

clear()
print("")
name = input("Enter your name: ")
# name = "You"

player = Player(name, 1000)
dealer = Player("Dealer", 1000)

time.sleep(0.5)
clear()
print("")
print("Welcome to Texas Hold Em, " + player.name + "!")
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
  round_id = "Round " + str(counter + 1)
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
  print("Your Credits: " + str(player.credits) + " | Dealer Credits: " + str(dealer.credits))
  print("")
  print("")
  print("\tDealer: [] []")
  print("")
  print("\tX [] [] [] [] [] ")
  print("")
  print("\t" + player.name + ": " + str(player.hand[0]) + " " + str(player.hand[1]))
  print("")
  print("")

  # first bets
  player_bet = input('Make your bet: ')
  time.sleep(0.3)
  clear()
  print("Your Credits: " + str(player.credits) + " | Dealer Credits: " + str(dealer.credits))
  print("")
  print("")
  print("\tDealer: [] []")
  print("")
  print("\tX [] [] [] [] [] ")
  print("")
  print("\t" + player.name + ": " + str(player.hand[0]) + " " + str(player.hand[1]))
  print("")
  print("")
  print('.')
  time.sleep(0.3)
  clear()
  print("Your Credits: " + str(player.credits) + " | Dealer Credits: " + str(dealer.credits))
  print("")
  print("")
  print("\tDealer: [] []")
  print("")
  print("\tX [] [] [] [] [] ")
  print("")
  print("\t" + player.name + ": " + str(player.hand[0]) + " " + str(player.hand[1]))
  print("")
  print("")
  print('..')
  time.sleep(0.3)
  clear()
  print("Your Credits: " + str(player.credits) + " | Dealer Credits: " + str(dealer.credits))
  print("")
  print("")
  print("\tDealer: [] []")
  print("")
  print("\tX [] [] [] [] [] ")
  print("")
  print("\t" + player.name + ": " + str(player.hand[0]) + " " + str(player.hand[1]))
  print("")
  print("")
  print('...')
  player.credits -= float(player_bet)

  ### write hand analysis for dealer so he can bet automatically without calling immediately
  dealer_bet = player_bet
  ###
  dealer.credits -= float(dealer_bet)

  # burn one
  card = deck.draw()
  dealer.add_card(card)

  # populate player"s hole cards
  for i in range(2):
    card = deck.draw()
    player.add_card(card)

  # show board and game info
  time.sleep(0.5)
  clear()
  print("Your Credits: " + str(player.credits) + " | Dealer Credits: " + str(dealer.credits))
  print("")
  print("")
  print("\tDealer: [] []")
  print("")
  print("\tX [] [] [] [] [] ")
  print("")
  print("\t" + str(player) + ": " + str(player.hand[0]) + " " + str(player.hand[1]))
  print("")
  print("")

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
  print("Your Credits: " + str(player.credits) + " | Dealer Credits: " + str(dealer.credits))
  print("")
  print("")
  print("\tDealer: [] []")
  print("")
  print("Flop:   X " + str(board.board[0]) + " " + str(board.board[1]) + " " + str(board.board[2]) + " [] [] ")
  print("")
  print("\t" + player.name + ": " + str(player.hand[0]) + " " + str(player.hand[1]))
  print("")
  print("")

  # analyze player"s hand and bet
  print(player.analyze(board.board))
  player_bet = input("Make your bet: ")

  # turn
  card = deck.draw()
  board.burn(card)
  card = deck.draw()
  board.turn(card)

  # update board
  time.sleep(1)
  clear()
  print("Your Credits: " + str(player.credits) + " | " + "Dealer Credits: " + str(dealer.credits))
  print("")
  print("")
  print("\tDealer: [] []")
  print("")
  print("Turn:   X " + str(board.board[0]) + " " + str(board.board[1]) + " " + str(board.board[2]) + " " + str(board.board[3]) + " [] ")
  print("")
  print("\t" + player.name + ": " + str(player.hand[0]) + " " + str(player.hand[1]))
  print("")
  print("")

  # analyze player"s hand and bet
  print(player.analyze(board.board))
  player_bet = input("Make your bet: ")

  # river
  card = deck.draw()
  board.burn(card)
  card = deck.draw()
  board.turn(card)

  # update board
  time.sleep(1)
  clear()
  print("Your Credits: " + str(player.credits) + " | Dealer Credits: " + str(dealer.credits))
  print("")
  print("")
  print("\tDealer: [] []")
  print("")
  print("River:  X " + str(board.board[0]) + " " + str(board.board[1]) + " " + str(board.board[2]) + " " + str(board.board[3]) + " " + str(board.board[4]))
  print("")
  print("\t" + player.name + ": " + str(player.hand[0]) + " " + str(player.hand[1]))
  print("")
  print("")
  
  # analyze player"s hand and bet
  print("Your hand analysis: " + player.analyze(board.board))
  player_bet = input("Make your bet: ")

  player.analyze(board.board)
  dealer.analyze(board.board)

  clear()
  print("Player: " + str(player.best_hand) + " | Dealer: " + str(dealer.best_hand))
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
        round.winner = "Split Pot"

  print("")
  print("Player:", [card.rank + card.suit for card in player.hand + board.board])
  print("")
  print("Dealer:", [card.rank + card.suit for card in dealer.hand + board.board])
  print("")

  game.add_round(round)

  for round in game.rounds:
    print(str(round.id) + " Winner: " + round.winner)

  print("")
  input("Press Enter to Continue.")

  player.reset()
  dealer.reset()

  counter += 1
  