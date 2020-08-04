import random
from helper import Deck
from Player import Player


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
        print("The winner is....")
        print("Player %s with a " % p.id, p.best_hand.score, p.best_hand.hand_lst)

if __name__ == "__main__":
    # TODO Add support for logging

    holdem = Game(4)
    holdem.run()