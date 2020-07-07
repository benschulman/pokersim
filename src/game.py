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
        hand.sort(key=lambda _ : RANK.index(_[0]))
        self.score = self._calc_score(hand)
        self.rank = self._calc_rank(hand)
    
    @staticmethod
    def _isFourOfAKind(hand):
        # Four + High Card
        found = True
        rank = hand[0][0]
        for i in range(1, len(hand)-1, 1):
            if not rank == hand[i][0]:
                found = False
                break
        if found:
            return True
        
        # Four + Low Card
        rank = hand[1][0]
        for i in range(2, len(hand), 1):
            if not rank == hand[i][0]:
                return False
        
        return True

    @staticmethod
    def _isFullHouse(hand):
        # Three and Two
        if hand[0][0] == hand[1][0] == hand[2][0]:
            if hand[3][0] == hand[4][0]:
                return True

        # Two and Three
        if hand[0][0] == hand[1][0]:
            if hand[2][0] == hand[3][0] == hand[4][0]:
                return True
        
        return False

    @staticmethod
    def _isFlush(hand):
        suit = hand[0][1]

        for card in hand:
            if not card[1] == suit:
                return False
        
        return True

    @staticmethod
    def _isStraight(hand):
        return False
    
    @staticmethod
    def _isThreeOfAKind(hand):
        if hand[0][0] == hand[1][0] == hand[2][0]:
            return True
        if hand[1][0] == hand[2][0] == hand[3][0]:
            return True
        if hand[2][0] == hand[3][0] == hand[4][0]:
            return True
        return False

    @staticmethod
    def _isTwoPair(hand):
        # 2 2 1
        if hand[0][0] == hand[1][0] and hand[2][0] == hand[3][0]:
            return True

        # 2 1 2
        if hand[0][0] == hand[1][0] and hand[3][0] == hand[4][0]:
            return True

        # 1 2 2
        if hand[1][0] == hand[2][0] and hand[3][0] == hand[4][0]:
            return True
        
        return False

    @staticmethod
    def _isPair(hand):
        # 2 1 1 1
        
        # 1 2 1 1
        # 1 1 2 1
        # 1 1 1 2
        return False
   
    def _calc_score(self, hand : list):
        # hand is assumed to be sorted by rank
        if not len(hand) == 5:
            raise Exception("Incorrect hand length")

        if Hand._isFlush(hand):
            if Hand._isStraight(hand):
                 # Straight Flush
                return Score.STRAIGHTFLUSH
            else:
                # Flush
                return Score.FLUSH
        if Hand._isStraight(hand):
            # Straight
            return Score.STRAIGHT
        
        if Hand._isFourOfAKind(hand):
            return Score.FOUROFAKIND
        
        if Hand._isFullHouse(hand):
            return Score.FULLHOUSE

        if Hand._isThreeOfAKind(hand):
            return Score.THREEOFAKIND
        
        if Hand._isTwoPair(hand):
            return Score.TWOPAIR
        
        if Hand._isPair(hand):
            return Score.PAIR

        return Score.HIGHCARD
    
    def _calc_rank(self, hand : list) -> tuple:
        # hand is assumed to be sorted by rank and self.score is correctly initialized
        # TODO Finish _calc_rank
        if not len(hand) == 5:
            raise Exception("Incorrect hand length")
        return (1,1,1,1,1)
    
    def compare(self, other):
        if self.score > other.score:
            return 1
        elif self.score == other.score:
            for a, b in zip(self.rank, other.rank):
                if a > b:
                    return 1
                elif b > a:
                    return -1
                else:
                    continue
            return 0
        else:
            return -1

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