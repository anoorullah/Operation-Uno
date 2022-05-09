import pygame

class Card:
    def __init__(self, color, value):
        """ Constructs a Card object that contains the color and number of the card. """
        self.color = color
        self.value = value

    def __eq__(self, other):
        """ Overloaded equal operator compares two cards for validity """
        return self.color=="WILD" or str(self.value) == str(other.value) or self.color == other.color

    def __str__(self):
        """ Overridden toString() method displays the card. """
        return str(self.color) + " " + str(self.value)