import random
import enum

# Sorted Deck Constant
SORTED_DECK = [
        'AS', 'KS', 'QS', 'JS', 'TS', '9S', '8S', '7S', '6S', '5S', '4S', '3S', '2S',
        'AH', 'KH', 'QH', 'JH', 'TH', '9H', '8H', '7H', '6H', '5H', '4H', '3H', '2H',
        'AD', 'KD', 'QD', 'JD', 'TD', '9D', '8D', '7D', '6D', '5D', '4D', '3D', '2D',
        'AC', 'KC', 'QC', 'JC', 'TC', '9C', '8C', '7C', '6C', '5C', '4C', '3C', '2C']

# Rank order Constant
RANK = '23456789TJQKA'

# Score of each type of Hand as an Enum
class Score(enum.Enum):
    HIGHCARD = 1
    PAIR = 2
    TWOPAIR = 3
    THREEOFAKIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULLHOUSE = 7
    FOUROFAKIND = 8
    STRAIGHTFLUSH = 9

class Hand:
    def __init__(self, hand):
        self.score = self._calc_score(hand)
        self.rank = self._calc_rank(hand)
    
    @staticmethod
    def _isStraightFlush(hand):
        pass

    @staticmethod
    def _isFourOfAKind(hand):
        pass

    @staticmethod
    def _isFullHouse(hand):
        pass

    @staticmethod
    def _isFlush(hand):
        pass

    @staticmethod
    def _isStraight(hand):
        pass
    
    @staticmethod
    def _isThreeOfAKind(hand):
        pass

    @staticmethod
    def _isTwoPair(hand):
        pass

    @staticmethod
    def _isPair(hand):
        pass
   
    def _calc_score(self, hand) -> Score:
        if not len(hand) == 5:
            raise Exception("Incorrect hand length")
        # TODO: Finish _calc_score method
        return Score.HIGHCARD
    
    def _calc_rank(self, hand) -> tuple:
        if not len(hand) == 5:
            raise Exception("Incorrect hand length")
        # TODO: Finish _calc_rank method
        return (1,1,1,1,1)
    
    def compare(self, other):
        # TODO Compare hands
        pass

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

class Player:
    def __init__(self, deck, stack):
        # contains the two cards that this player has in their hand
        self.cards = [next(deck), next(deck)]
        # How much money they have
        self.stack = stack
        # Is this person currently out of the hand
        self.folded = False
        # The Hand object of their current best possible Hand
        self.best_hand = None
    
    def set_best_hand(self, board):
        # TODO set_best_hand
        # Should go through all possible combinations of 5 card hands and compare them with the Hand.compare
        #flop
        if len(board) == 3:
            pass
        #turn
        if len(board) == 4:
            pass
        #river
        if len(board) == 5:
            pass

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
    
    def _deal_cards(self, num):
        # Deal num cards from the deck onto the board
        for i in range(num):
            self.board.append(next(self.deck))


    def _determine_winner(self):
        # TODO Fix for ties
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
        return player

    def display_boad(self):
        # TODO Graphics
        print(self.board)

    def bet_round(self, preflop=False):
        # TODO bet_round
        input() # temporary for pausing
        pass
    
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

        # Print cards (temporarily)
        for player in self.players:
            print(player.cards)

        self.bet_round(preflop=True)

        self.flop()
        self.turn()
        self.river()

        self.determine_winner()

if __name__ == "__main__":
    holdem = Game(1)
    holdem.run()