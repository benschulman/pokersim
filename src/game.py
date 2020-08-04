import random
from helper import Hand
from constants import SORTED_DECK



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

    def place_bet(self, ammount):
        # TODO Place bet in Player class
        if ammount > self.stack - self.invested:
            raise Exception("Not enough money")

class Deck:
        def __iter__(self):
                self.deck = SORTED_DECK.copy()
                random.shuffle(self.deck)
                self.count = 0
                return self

        def __next__(self):
                if self.count >= 52:
                        raise StopIteration
                card = self.deck[self.count]
                self.count += 1
                return card


class Game:
    def __init__(self, num_players):
        # create the iterable deck to deal cards from
        self.deck = iter(Deck())
        # create a list of Player objects
        if num_players > 9 or num_players < 1:
            raise Exception("Invalid Player Ammount")
        self.players = [Player(self.deck, 100) for i in range(num_players)]
        # The board of common cards
        self.board = []
        self.pot = 0
    
    def _deal_cards(self, num):
        # Deal num cards from the deck onto the board
        for _ in range(num):
            self.board.append(next(self.deck))

    def _determine_winner(self):
        # TODO Fix _determine_winner to support ties (split pot)
        # Compares all of the players' best_hands and returns the winner
        best = None
        for player in self.players:
            if not player.folded:
                if best == None:
                    best = player
                else:
                    # if the player has a better best_hand than best, then set best to player
                    if best.best_hand.compare(player.best_hand) < 0:
                        best = player
        return best

    def display_boad(self):
        print(self.board)

    def bet_round(self, preflop=False):
        # TODO Implement bet_round
        input() # temporary for pausing
    
    def calc_hands(self):
        # This function should be called after any card is delt to calculate each player's new best hand
        for player in self.players:
            player.set_best_hand(self.board)

    def flop(self):
        # Deal cards
        self._deal_cards(3)
        # Display board
        print("Flop")
        self.display_boad()
        self.calc_hands()
        self.bet_round()
            
    def turn(self):
        self._deal_cards(1)
        print("Turn")
        self.display_boad()
        self.calc_hands()
        self.bet_round()
    
    def river(self):
        self._deal_cards(1)
        print("River")
        self.display_boad()
        self.calc_hands()
        self.bet_round()

    def run(self):
        print("Starting Game...")
        for player in self.players:
            print(player.cards)

        self.bet_round(preflop=True)

        self.flop()
        self.turn()
        self.river()

        p = self._determine_winner()
        print("The winner is....")
        print("Player %s with a " % p.id, p.best_hand.score, p.best_hand.hand_lst)

if __name__ == "__main__":
    # TODO Add support for logging

    holdem = Game(9)
    holdem.run()