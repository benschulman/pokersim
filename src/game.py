import random
from pokertools.helper import Deck
from pokertools.player import Player

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
        self.dealer_index = 0
    
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
        # index of current better
        curr_better_ind = (self.dealer_index + 1) % len(self.players)
        # index of player that made the most recent raise
        # this index tells the while loop when we are done, once we reach
        # this player again then we are finished betting
        end_ind = curr_better_ind
        _player = self.players[curr_better_ind]
        # size of current bet
        call_amnt = 0
        """
        while True:
            if not _player.folded:
                ret = self.players[curr_better_ind].option(call_amnt)
                # check or all-in case
                if ret == 0:
                    pass
                elif ret == -1:
                    pass
                elif ret > 0:
                    pass

        """
        input()
        # Logic might be better suited to have in flop, turn and river methods
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
        for player in self.players:
            print(player.cards)

        self.bet_round(preflop=True)

        self.flop()
        self.turn()
        self.river()

        p = self._determine_winner()

        # Move the dealer chip
        self.dealer_index += 1
        self.dealer_index %= len(self.players)

        print("The winner is....")
        print("Player %s with a " % p.id, p.best_hand.score, p.best_hand.hand_lst)

if __name__ == "__main__":
    # TODO Add support for logging

    holdem = Game(4)
    holdem.run()
