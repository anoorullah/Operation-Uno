from Card import Card
from Ruleset import Ruleset
from AI import AI
import numpy as np
import pygame

class Player():
    def __init__(self, name, isAI=False, difficulty="Easy"):
        """ Constructs a AI object with a name and an empty hand. """
        # print("Creating", name) # Testing
        self.name = name
        self.hand = pygame.sprite.Group()
        self.isAI = isAI
        self.difficulty = difficulty
    
    def addCard(self, card):
        """ Adds a card to the AI's hand. """
        # print("Adding", card, "to", self.name, "'s hand") # Testing
        if not self.isAI:
            card.toggle_face()
        self.hand.add(card)

    def removeCard(self, card):
        """ Removes card from hand. """
        self.hand.remove(card)

    def playCardAI(self, top_card):
        """ AI plays a card dependping on difficulty level. """
        return AI.playCard(self, top_card)

    def maxColor(self):
        """ Finds the color that the AI has the most of. """
        colors = {"RED" : 0, "YELLOW" : 0, "GREEN" : 0, "BLUE" : 0}
        for card in self.hand:
            if not card.card.color=="WILD":
                colors[card.card.color]+=1
        return max(colors, key=colors.get)

    def isWin(self):
        """ Returns True if the player has an empty hand (won the game) and false otherwise """
        return not self.hand

    def displayHand(self):
        """ Returns a string containing all cards in the player's hand. """
        cards = ""
        for card in self.hand:
            cards += str(card) + " | "
        return cards

    def __str__(self):
        """ Overridden toString() method displays AI's name and hand. """
        return str(self.name) + "'s hand: " + str(self.displayHand())

    def changeName(self, name):
        self.name = name
    
    def getName(self):
        return self.name