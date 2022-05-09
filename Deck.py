from Card import Card
import numpy as np
import random
from Ruleset import Ruleset
from Sprites.CardSprite import CardSprite
import pygame

class Deck():
    # ruleset  -> ruleset to apply to deck functions, default=default ruleset
    # seed     -> random seed for generating the deck, default=random

    def __init__(self, w, h, ruleset=Ruleset(), seed=None):
        """ Constructs a Deck object that contains a shuffled deck. """
        self.ruleset = ruleset
        self.deck = []
        for card in self.ruleset.deck:
            self.deck.append(card)
        self.shuffle(seed)
        self.sprite_deck = pygame.sprite.Group()
        self.inititialize_sprite_deck(w, h)

    def inititialize_sprite_deck(self, w, h): # will pass in Ruleset class to receive parameters for a specialized deck
        """ Initializes a shallow copy of the ruleset deck. """
        for card in self.deck:
            self.sprite_deck.add(CardSprite((0, 0), (w/8, h/8), card))

    def shuffle(self, seed=None):
        """ 
        Shuffles the deck using numpy's random shuffle method. 
        If a seed does not exist, randomize normally.
        """
        if seed:
            random.seed(seed)
        random.shuffle(self.deck)

    def draw(self):
        """ Draws and removes the card at the top of the deck. """
        removed_sprite = self.sprite_deck.sprites()[0]
        self.sprite_deck.remove(removed_sprite)
        return removed_sprite
    
    def peek(self):
        """ Shows the card at the top of the deck without removing. """
        return self.sprite_deck.sprites()[0]

    def __str__(self):
        """ Overridden toString() method displays the deck. """
        cards = "------ DECK ------ ("
        cards += str(len(self.deck)) + " cards)\n"
        for card in self.deck:
            cards += str(card) + "\n"
        return cards
