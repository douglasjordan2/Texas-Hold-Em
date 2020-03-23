class Player:
  def __init__(self, name, credits):
    self.name = name
    self.credits = credits
    self.hand = []
    self.kicker = None
    self.tie_breaker = None
    self.best_hand = None

  def __str__(self):
    return self.name

  def add_card(self, card):
    self.hand.append(card)

  def win(self, pot):
    self.credits += pot
    self.hand = []

  def lose(self, pot):
    self.credits -= pot
    self.hand = []

  def reset(self):
    self.hand = []
    self.best_hand = None

  def analyze(self, board):
    hand = self.hand + board
    hand.sort(key=lambda x: x.sort)

    def check_straight(hand):
      straight = True
      for i in range(len(hand) - 1):
        if hand[i + 1].rank != hand[i].next:
          straight = False
      
      return straight

    def ace_to_back(hand):
      for card in hand:
        if card.rank == 'A':
          card.sort = 14
        if card.rank == 'K':
          card.next = 'A'
      hand.sort(key=lambda x: x.sort)
      return hand
    
    has_ace = False
    has_king = False
    straight = False

    for card in hand:
      if card.rank == 'A':
        has_ace = True
      if card.rank == 'K':
        has_king = True
  
    if has_ace and has_king:
      temp_hand = ace_to_back(hand)
      if check_straight(temp_hand[len(temp_hand) - 5:]):
        straight = True
        hand = temp_hand[len(temp_hand) - 5:]
    
    if len(hand) == 5: 
      straight = check_straight(hand)
    elif len(hand) == 6:
      if check_straight(hand[1:]):
        straight = True
        hand = hand[1:]
      elif check_straight(hand[:5]):
        straight = True
        hand = hand[1:]
    else:
      if check_straight(hand[2:]):
        straight = True
        hand = hand[2:]
      elif check_straight(hand[1:6]):
        straight = True
        hand = hand[1:6]
      elif check_straight(hand[:5]):
        straight = True
        hand = hand[:5]

    flush_hold = {}
    for card in hand:
      if card.suit not in flush_hold:
        flush_hold[card.suit] = 1
      else:
        flush_hold[card.suit] += 1

    flush = False
    for k, v in flush_hold.items():
      if v >= 5:
        flush = True

    return_hand = [f'{card.rank}{card.suit}'  for card in hand]

    if straight:
      if flush:
        if hand[0].rank == '10' and hand[-1].rank == 'A':
          self.best_hand = 10
          return 'You have a royal flush.', return_hand
        else:
          self.best_hand = 9
          return 'You have a straight flush.', return_hand
      else:
        self.best_hand = 5
        return 'You have a straight', return_hand
    elif flush:
      self.best_hand = 6
      return 'You have a flush.', return_hand
    else:
      hand = ace_to_back(hand)

    hand.sort(key = lambda x: x.sort)

    check_hand = {}
    for card in hand:
      if card.rank not in check_hand:
        check_hand[card.rank] = [card]
      else:
        check_hand[card.rank].append(card)

    most = None
    least = None

    for k, v in check_hand.items():
      if most is None:
        most = (k, v)
      elif least is None:
        if len(v) < len(most[1]):
          least = (k, v)
        else:
          least = most
          most = (k, v)
      else:
        if len(v) >= len(most[1]):
          least = most
          most = (k, v)
        elif len(v) == len(least[1]):
          least = (k, v)

    if len(most[1]) is 4:
      self.best_hand = 8

      if self.hand[0].rank is not most[0] and self.hand[1].rank is most[0]:
        k = hand[-1]
        self.kicker = k
        self.tie_breaker = most[1][0]
        grammar = 'an' if k.rank is 'A' else 'a'
        return f'You have quad {most[0]}s with {grammar} {k.rank} kicker.'
      else:
        return f'You have quad {most[0]}s.'

    if len(most[1]) is 3:
      if len(least[1]) is 2:
        self.best_hand = 7
        self.tie_breaker = most[1][0]

        return f'You have a full house, {most[0]}s over {least[0]}s.'
      else:
        self.best_hand = 4

        k = hand[0]
        self.kicker = k
        self.tie_breaker = most[1][0]
        for card in hand:
          if card.sort > k.sort and card.rank is not most[0]:
            k = card
        grammar = 'an' if k.rank is 'A' else 'a'
        return f'You have trip {most[0]}s with {grammar} {k.rank} kicker.'
        

    if len(most[1]) is 2:
      if len(least[1]) is 2:
        self.best_hand = 3

        k = hand[0]
        for card in hand:
          if card.sort > k.sort and card.rank is not most[0] and card.rank is not least[0]:
            k = card

        self.kicker = k
        self.tie_breaker = most[1][0]
        grammar = 'an' if k.rank is 'A' else 'a'
        return f'You have two pair, {most[0]}s and {least[0]}s with {grammar} {k.rank} kicker.'
      else:
        self.best_hand = 2

        k = hand[0]
        for card in hand:
          if card.sort > k.sort and card.rank is not most[0]:
            k = card
        
        self.kicker = k
        self.tie_breaker = most[1][0]
        grammar = 'an' if k.rank is 'A' else 'a'
        return f'You have a pair of {most[0]}s with {grammar} {k.rank} kicker.'

    if len(most[1]) is 1:
      self.best_hand = 1
      self.tie_breaker = most[1][0]
      self.kicker = most[1][0]
      
      return f'High card, {most[0]}'