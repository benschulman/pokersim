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

class Hand(enum.Enum):
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


class Player:
    def __init__(self, deck):
        # contains the two cards that this player has in their hand
        self.cards = [next(deck), next(deck)]
        # How much money they have
        self.stack = 100.0
        # Is this person currently out of the hand
        self.folded = False
        # The type of hand that this person has
        self.score = Hand.HIGHCARD
        # The actual cards that make up this hand
        self.hand = []

class Game:
    def __init__(self, num_players):
        self.deck = iter(Deck())
        self.players = [Player(self.deck) for i in range(num_players)]
        self.board = []
    
    def _deal_cards(self, num):
        # deal n cards from the deck onto the board
        for i in range(num):
            self.board.append(next(self.deck))
    
    def _check_player_best_hand(self, player):
        # for each card in player's hand
        for card in player.cards:
            # exclude one card from the board
            for c2 in self.board:
                # include card and exclude c2
                lst = [i for i in self.board if i != c2]
                lst.append(card)
                lst.sort(key=lambda _ : RANK.index(_[0]))
                # Straight flush
                if isFlush(lst):
                    if isStraight(lst):
                        if player.score < Hand.STRAIGHTFLUSH:
                            player.score = Hand.STRAIGHTFLUSH
                            player.hand = lst.copy()
                            continue
                        else:  # player.score == Hand.STRAIGHTFLUSH:
                            #TODO Check which one is better
                            pass
                    # Flush
                    else:
                        if player.score < Hand.FLUSH:
                            player.score = Hand.FLUSH
                            player.hand = lst.copy()
                            continue
                        elif player.score == Hand.FLUSH:
                            #TODO check which is better
                            pass
                
                # Straight
                if isStraight(lst):
                    if player.score < Hand.STRAIGHT:
                        player.score = Hand.STRAIGHTFLUSH
                        player.hand = lst.copy()
                        continue
                    elif player.score == Hand.STRAIGHT:
                        # TODO
                        pass
                # 4oK
                if is4ok(lst):

                # Boat 
                
                # 3oK
                # 2P
                # Pair
                # HK
                print(lst)
                exit()

    def determine_winner(self):
        print("Calculating Winner...")
        for player in self.players:
            if player.folded:
                continue
            else:
                #TODO: determine winner
                self._check_player_best_hand(player)

    def flop(self):
        self._deal_cards(3)
        print("Flop: ", self.board)
    
    def turn(self):
        self._deal_cards(1)
        print("Turn: ", self.board)
    
    def river(self):
        self._deal_cards(1)
        print("River: ", self.board)

    def main(self):
        print("Starting Game...")

        for player in self.players:
            print(player.cards)

        input()
        self.flop()
        input()
        self.turn()
        input()
        self.river()
        input()

        self.determine_winner()

if __name__ == "__main__":
    holdem = Game(1)
    holdem.main()