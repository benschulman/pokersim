import enum
import random
from constants import RANK, SORTED_DECK

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