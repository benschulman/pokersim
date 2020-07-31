import random
import enum
import logging

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
        self.score, self.rank = self._calc_score_and_rank(hand)
        self.hand_lst = hand
    
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
            r_1 = RANK.index(rank)
            r_2 = RANK.index(hand[4][0])
            tup = [r_1,r_1,r_1,r_1,r_2]
            return (True, tup)
        
        # Four + Low Card
        rank = hand[1][0]
        for i in range(2, len(hand), 1):
            if not rank == hand[i][0]:
                return (False, [1,1,1,1,1])
        
        r_1 = RANK.index(rank)
        r_2 = RANK.index(hand[0][0])
        tup = [r_1,r_1,r_1,r_1,r_2]
        return (True, tup)

    @staticmethod
    def _isFullHouse(hand):
        # Three and Two
        if hand[0][0] == hand[1][0] == hand[2][0]:
            if hand[3][0] == hand[4][0]:
                r_1 = RANK.index(hand[0][0])
                r_2 = RANK.index(hand[3][0])
                tup = [r_1, r_1, r_1, r_2, r_2]
                return (True, tup)

        # Two and Three
        if hand[0][0] == hand[1][0]:
            if hand[2][0] == hand[3][0] == hand[4][0]:
                r_1 = RANK.index(hand[2][0])
                r_2 = RANK.index(hand[0][0])
                tup = [r_1, r_1, r_1, r_2, r_2]
                return (True, tup)
        
        return (False, [1,1,1,1,1])

    @staticmethod
    def _isFlush(hand):
        suit = hand[0][1]
        tup = [1,1,1,1,1]

        for card in hand:
            if not card[1] == suit:
                return (False, tup)
        
        for i, card in enumerate(hand):
            tup[4-i] = RANK.index(card[0])
        return (True, tup)

    @staticmethod
    def _isStraight(hand):
        get_rank = lambda _ : RANK.index(_[0])
        rank_num = get_rank(hand[0])
        tup = [1,1,1,1,rank_num]

        for i in range(1, 5, 1):
            if not get_rank(hand[i]) == rank_num + 1:
                # wheel case
                if not (i == 4 and rank_num == RANK.index('5') and hand[i][0] == 'A'):
                    return (False, [1,1,1,1,1])
                else:
                    return (True, [3,2,1,0,-1])
            rank_num = get_rank(hand[i])
            tup[4-i] = rank_num
        
        return (True, tup)
    
    @staticmethod
    def _isThreeOfAKind(hand):
        get_rank = lambda _ : RANK.index(_[0])

        if hand[0][0] == hand[1][0] == hand[2][0]:
            r_1 = get_rank(hand[0])
            r_2 = get_rank(hand[3])
            r_3 = get_rank(hand[4])
            return (True, [r_1, r_1, r_1, r_3, r_2])
        if hand[1][0] == hand[2][0] == hand[3][0]:
            r_1 = get_rank(hand[1])
            r_2 = get_rank(hand[0])
            r_3 = get_rank(hand[4])
            return (True, [r_1, r_1, r_1, r_3, r_2])
        if hand[2][0] == hand[3][0] == hand[4][0]:
            r_1 = get_rank(hand[2])
            r_2 = get_rank(hand[0])
            r_3 = get_rank(hand[1])
            return (True, [r_1, r_1, r_1, r_3, r_2])
        return (False, [1,1,1,1,1])

    @staticmethod
    def _isTwoPair(hand):
        get_rank = lambda _ : RANK.index(_[0])
        # 2 2 1
        if hand[0][0] == hand[1][0] and hand[2][0] == hand[3][0]:
            r_1 = get_rank(hand[0])
            r_2 = get_rank(hand[2])
            r_3 = get_rank(hand[4])

            return (True, [r_2, r_2, r_1, r_1, r_3])

        # 2 1 2
        if hand[0][0] == hand[1][0] and hand[3][0] == hand[4][0]:
            r_1 = get_rank(hand[0])
            r_2 = get_rank(hand[3])
            r_3 = get_rank(hand[2])

            return (True, [r_2, r_2, r_1, r_1, r_3])

        # 1 2 2
        if hand[1][0] == hand[2][0] and hand[3][0] == hand[4][0]:
            r_1 = get_rank(hand[1])
            r_2 = get_rank(hand[3])
            r_3 = get_rank(hand[0])

            return (True, [r_2, r_2, r_1, r_1, r_3])
        
        return (False, [1,1,1,1,1])

    @staticmethod
    def _isPair(hand):
        get_rank = lambda _ : RANK.index(_[0])

        # 2 1 1 1
        if hand[0][0] == hand[1][0]:
            r_1 = get_rank(hand[0])
            r_2 = get_rank(hand[2])
            r_3 = get_rank(hand[3])
            r_4 = get_rank(hand[4])

            return (True, [r_1, r_1, r_4, r_3, r_2])
        # 1 2 1 1
        if hand[1][0] == hand[2][0]:
            r_1 = get_rank(hand[1])
            r_2 = get_rank(hand[0])
            r_3 = get_rank(hand[3])
            r_4 = get_rank(hand[4])

            return (True, [r_1, r_1, r_4, r_3, r_2])
        # 1 1 2 1
        if hand[2][0] == hand[3][0]:
            r_1 = get_rank(hand[2])
            r_2 = get_rank(hand[0])
            r_3 = get_rank(hand[1])
            r_4 = get_rank(hand[4])

            return (True, [r_1, r_1, r_4, r_3, r_2])
        # 1 1 1 2
        if hand[3][0] == hand[4][0]:
            r_1 = get_rank(hand[3])
            r_2 = get_rank(hand[0])
            r_3 = get_rank(hand[1])
            r_4 = get_rank(hand[2])

            return (True, [r_1, r_1, r_4, r_3, r_2])

        return (False, [1,1,1,1,1])
   
    def _calc_score_and_rank(self, hand : list):
        # hand is assumed to be sorted by rank
        if not len(hand) == 5:
            raise Exception("Incorrect hand length")
        
        isFlush = Hand._isFlush(hand)
        isStraight = Hand._isStraight(hand)

        if isFlush[0]:
            if isStraight[0]:
                 # Straight Flush
                return (Score.STRAIGHTFLUSH, isFlush[1])
            else:
                # Flush
                return (Score.FLUSH, isFlush[1])
        if isStraight[0]:
            # Straight
            return (Score.STRAIGHT, isStraight[1])
        
        isFourOfAKind = Hand._isFourOfAKind(hand)
        if isFourOfAKind[0]:
            return (Score.FOUROFAKIND, isFourOfAKind[1])
        
        isFullHouse = Hand._isFullHouse(hand)
        if isFullHouse[0]:
            return (Score.FULLHOUSE, isFullHouse[1])

        isThreeOfAKind = Hand._isThreeOfAKind(hand)
        if isThreeOfAKind[0]:
            return (Score.THREEOFAKIND, isThreeOfAKind[1])
        
        isTwoPair = Hand._isTwoPair(hand)
        if isTwoPair[0]:
            return (Score.TWOPAIR, isTwoPair[1])
        
        isPair = Hand._isPair(hand)
        if isPair[0]:
            return (Score.PAIR, isPair[1])

        tup = [1,1,1,1,1]
        for i, card in enumerate(hand):
            tup[4-i] = RANK.index(card[0])
        return Score.HIGHCARD, tup
    
    def compare(self, other):
        if self.score.value > other.score.value:
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
        for i in range(num):
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
    logging.basicConfig(filename='logs/debug.log',level=logging.DEBUG)

    holdem = Game(9)
    holdem.run()