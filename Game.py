from Deck import Deck
from Player import Player
from Ruleset import Ruleset
import numpy as np
import pygame

class Game:
    # isMultiplayer -> whether or not game is multiplayer
    # num_players   -> number of AI in singleplayer, total player in multiplayer, default=1
    # difficulty    -> bot difficulty, TBD
    # playerNames   -> list of player names, default=empty

    # prototype parameters: please ask Jacob if there are issues
    # ruleset       -> current game ruleset, leave empty for default ruleset 
    # deckSeed      -> random seed for deck generation, default=random

    def __init__(self, w, h, isMultiplayer, num_players=1, difficulty="Easy", playerNames=[], ruleset=Ruleset(), deckSeed=None):
        """ Constructs a Game object with players and AI, deals cards, and starts a game. """
    
        self.isMultiplayer = isMultiplayer
        self.ruleset = ruleset
        self.deckSeed = deckSeed
        self.w = w
        self.h = h
        self.deck = Deck(self.w, self.h, self.ruleset, deckSeed)
        self.played_cards = pygame.sprite.Group()
        self.player_name = "Player Name"

        # Initialize players
        self.players = []
        if isMultiplayer:
            for player in playerNames:
                self.players.append(Player(player))
        else:
            self.players.append(Player("Player Name")) # need to fetch from profile.py class or something
            for i in range(num_players):
                self.players.append(Player("AI " + str(i), True, difficulty))
        self.total_players = len(self.players)
        self.main_player = self.players[0]
        np.random.shuffle(self.players)
        
        # Deals cards to the players and initializes the top card
        self.deal()
        self.played_cards.add(self.deck.draw())
        self.top_card = self.played_cards.sprites()[0]

        # Initializes turn orders
        self.turn = 1
        self.actual_turn = 1

    def setMainPlayerName(self, name):
        self.player_name = name
        for player in self.players:
            if player.getName() == "Player Name":
                player.changeName(self.player_name)
    
    def getMainPlayerName(self):
        return self.player_name

    def deal(self):
        """ Deals cards to each player (including AI). """
        for player in self.players:
            self.draw(player, self.ruleset.deal_quantity) # Deals 7 cards, but Ruleset will override this number later on
        # for player in self.players: 
            # print(player) # Testing
    
    def draw(self, player, num_times):
        """ Passed in player draws a random card from self.deck exactly 'num_times'. """
        for i in range(num_times):
            # print(player.name, "drew", self.deck.peek())
            player.addCard(self.deck.draw())

    def skipTurn(self):
        """ Updates turn count of game instance. Effectively skips a turn. """
        self.turn += 1

    def getCurrPlayer(self):
        """ Returns the current turn's player. """
        currPlayer = self.players[self.getPlayerNum()]
        return currPlayer

    def getPlayerNum(self):
        """ Returns the index of the current player. """
        return (self.turn-1) % len(self.players)

    def update_turn(self, curr_player, played_card=None):
        """ Handles game logic for an AI-player's turn. If player is not AI, return control of program to the user by returning True. """        
        if curr_player.isAI:
            played_card = curr_player.playCardAI(self.top_card)
            if not played_card:
                self.draw(curr_player, 1)
                played_card = curr_player.playCardAI(self.top_card)
        self.turn += 1
        self.actual_turn += 1
        return self.updateGameState(played_card, curr_player)

    def get_winner(self):
        """ Returns winner (if there is one). """
        for player in self.players:
            if player.isWin():
                return player
        return None

    def updateGameState(self, played_card, curr_player):
        """ Core game logic for a given turn and player. Handles general cards, SKIPs, REVERSEs, and DRAWs. 
            Updates the corresponding top card of the deck. Returns True if the turn order was reversed """
        curr_player.removeCard(played_card)
        if not played_card:
            return False
            # print(curr_player.name, "skipped their turn")
        elif played_card:
            if played_card.card.value=="REVERSE":
                self.players.reverse()
                # print("Turn order:", end="")
                # for player in self.players:
                #     print(player.name, end=" | ")  
                # print()
                # print("Reverse")
                self.turn = self.total_players - (self.turn % self.total_players) - 1

            elif played_card.card.value=="SKIP":
                # print("Skipped", self.players[(self.turn) % self.total_players].name, "turn")
                self.turn+=1

            elif played_card.card.value=="DRAW 2":
                self.draw(self.players[(self.turn-1) % self.total_players], 2)
                # print("Added 2 cards to", self.players[(self.turn) % self.total_players].name)
                self.turn+=1

            elif played_card.card.value=="DRAW 4":
                self.draw(self.players[(self.turn-1) % self.total_players], 4)
                # print("Added 4 cards to", self.players[(self.turn) % self.total_players].name)
                self.turn+=1

            if not curr_player==self.main_player:
                played_card.toggle_face()
            played_card.update_pos((self.w/2, self.h/2))     
            self.played_cards.add(played_card)
            self.top_card = played_card

            return played_card.card.value=="REVERSE"

    def changeSoundEffects(self, sound):
        """ Changes if sound effects are on/off """
        self.sound = sound

    def getSoundEffects(self):
        """ Returns sound (on/off) state """
        return self.sound

    def printGameState(self):
        print('NumPlayers: ', self.num_players, '\nSound: ', self.sound, '\nDifficulty: ', self.difficulty)
    