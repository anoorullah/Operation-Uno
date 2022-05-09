from Card import Card

class Ruleset():
    # cardSet      -> unshuffled set of cards to include when generating deck
    # dealQuantity -> number of cards each player starts with, default=7
    def __init__(self):
        self.initialize_standard_game() # by default, but can be overwritten with new rules

    def isValid(self, card, top_card):
        """ Checks if card is able to be placed during the current turn (based on top card). """
        return card.card == top_card.card

    def initialize_standard_game(self):
        """ Initializes deck for game. """
        colors = ["RED","BLUE","GREEN","YELLOW"]
        cards_zero   = [Card(c,0) for c in colors]
        cards_number = [Card(c,v) for c in colors for v in range (1,10)]*2
        cards_action = [Card(c,v) for c in colors for v in ["SKIP","REVERSE","DRAW 2"]]*2
        cards_wild   = [Card("WILD",v) for v in ["CARD","DRAW 4"]]*4
        self.deck = cards_zero + cards_number + cards_action + cards_wild
        self.deal_quantity = 7

    def initialize_quick_game(self):
        """ Initializes a deck for game with half as many numbered and 'special' cards. """
        colors = ["RED","BLUE","GREEN","YELLOW"]
        cards_zero   = [Card(c,0) for c in colors]
        cards_number = [Card(c,v) for c in colors for v in range (1,10)]
        cards_action = [Card(c,v) for c in colors for v in ["REVERSE","DRAW 2"]]
        cards_wild   = [Card("WILD",v) for v in ["CARD"]]*2
        self.deck = cards_zero + cards_number + cards_action + cards_wild
        self.deal_quantity = 4

    def initialize_doubledeck_game(self):
        """ Initializes a deck for game with twice as many numbered and 'special' cards. """
        colors = ["RED","BLUE","GREEN","YELLOW"]
        cards_zero   = [Card(c,0) for c in colors]*2
        cards_number = [Card(c,v) for c in colors for v in range (1,10)]*4
        cards_action = [Card(c,v) for c in colors for v in ["SKIP","REVERSE","DRAW 2"]]*4
        cards_wild   = [Card("WILD",v) for v in ["CARD","DRAW 4"]]*8
        self.deck = cards_zero + cards_number + cards_action + cards_wild
        self.deal_quantity = 7