from helper import Hand
class Player:
    count = 0
    def __init__(self, deck, stack):
        # contains the two cards that this player has in their hand
        self.cards = [next(deck), next(deck)]
        # How much money they have
        self.stack = stack
        # Is this person currently out of the hand
        self.folded = False
        # The Hand object of their current best possible Hand
        self.best_hand = None
        # How much the player has bet on a given hand
        self.invested = 0
        self.id = Player.count + 1
        Player.count += 1
    
    def set_best_hand(self, board):
        # Should go through all possible combinations of 5 card hands and compare them with the Hand.compare
        
        # flop
        if len(board) == 3:
            temp_hand = board.copy()
            temp_hand.append(self.cards[0])
            temp_hand.append(self.cards[1])
            self.best_hand = Hand(temp_hand)
            return
        # turn
        if len(board) == 4:
            temp_hand = []
            # 2 hand 3 board
            for card in board:
                temp_hand = [c for c in board if not c == card]
                temp_hand.extend(self.cards)
                new_hand = Hand(temp_hand)
                if self.best_hand == None:
                    self.best_hand = new_hand
                else:
                    if self.best_hand.compare(new_hand) < 0:
                        self.best_hand = new_hand
            
            # 1 hand 4 board
            for card in self.cards:
                temp_hand = [c for c in board]
                temp_hand.append(card)
                new_hand = Hand(temp_hand)
                if self.best_hand == None:
                    self.best_hand = new_hand
                else:
                    if self.best_hand.compare(new_hand) < 0:
                        self.best_hand = new_hand
            return
        
        # river
        if len(board) == 5:
            # just board
            new_hand = Hand(board)
            if self.best_hand == None:
                self.best_hand = new_hand
            else:
                if self.best_hand.compare(new_hand) < 0:
                    self.best_hand = new_hand
            
            # 4 board 1 hand
            for card in board:
                for card2 in self.cards:
                    temp_hand = [c for c in board if not c == card]
                    temp_hand.append(card2)
                    new_hand = Hand(temp_hand)
                    if self.best_hand == None:
                        self.best_hand = new_hand
                    else:
                        if self.best_hand.compare(new_hand) < 0:
                            self.best_hand = new_hand
            # 3 board 2 cards
            for i in range(0,5):
                for j in range(i+1,5):
                    temp_hand = [board[k] for k in range(0,5) if not k == i and not k == j]
                    temp_hand.extend(self.cards)
                    new_hand = Hand(temp_hand)
                    if self.best_hand == None:
                        self.best_hand = new_hand
                    else:
                        if self.best_hand.compare(new_hand) < 0:
                            self.best_hand = new_hand
            return
        return

    def option(self):
        # TODO implement option to bet check or fold
        pass

    def _check(self):
        pass

    def _place_bet(self, ammount, min_bet=0):
        # TODO Min-bets
        if ammount > self.stack:
            raise Exception("Not enough money")
        if ammount < min_bet:
            raise Exception("Bet size too small")
        self.invested += ammount
        self.stack -= ammount
    
    def _fold(self):
        self.folded = True
        self.invested = 0