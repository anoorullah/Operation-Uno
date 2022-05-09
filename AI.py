from Card import Card
from Ruleset import Ruleset
import numpy as np

class AI():
    @staticmethod
    def playCard(self, top_card):
        """ Play's the card from AI's hand. """


        if self.difficulty == "Easy":
            """ 
            Easy AI plays the first valid card, prioritzing:
            1. any colored or wild cards
            """
            for card in self.hand:
                if Ruleset.isValid(self, card, top_card):
                    if card.card.color=="WILD":
                        card.update_card(Card(self.maxColor(), card.card.value), False)
                    return card



        elif self.difficulty == "Medium":
            """ 
            Medium AI plays the first valid card, prioritzing:
            1. colored cards from any color set
            2. wild cards
            """
            for card in self.hand:
                if Ruleset.isValid(self, card, top_card) and card.card.color != "WILD":
                    return card
            for card in self.hand:
                if Ruleset.isValid(self, card, top_card):
                    if card.card.color=="WILD":
                        card.update_card(Card(self.maxColor(), card.card.value), False)
                    return card



        else:
            """ 
            Hard AI plays the first valid card, prioritzing:
            1. colored cards of the set they have the most of, not including +2, skip, draw 2
            2. colored cards of the set they have the most of, including +2, skip, draw 2
            3. other colored cards
            4. wild cards
            """

            deprioritized = ["SKIP","REVERSE","DRAW 2"]
            

            for card in self.hand:
                if Ruleset.isValid(self, card, top_card) and card.card.color==self.maxColor() and (not card.card.value in deprioritized):
                    return card
            for card in self.hand:
                if Ruleset.isValid(self, card, top_card) and card.card.color==self.maxColor():
                    return card
            for card in self.hand:
                if Ruleset.isValid(self, card, top_card) and card.card.color != "WILD":
                    return card
            for card in self.hand:
                if Ruleset.isValid(self, card, top_card):
                    if card.card.color=="WILD":
                        card.update_card(Card(self.maxColor(), card.card.value), False)
                    return card










    # def __init__(self, name):
    #     """ Constructs a AI object with a name and an empty hand. """
    #     # print("Creating", name) # Testing
    #     self.name = name
    #     self.hand = []
    
    # def addCard(self, card):
    #     """ Adds a card to the AI's hand. """
    #     # print("Adding", card, "to", self.name, "'s hand") # Testing
    #     self.hand.append(card)


    # def maxColor(self):
    #     """ Finds the color that the AI has the most of. """
    #     colors = [0] * 4
    #     for card in self.hand:
    #         if card.color=="RED":
    #             colors[0]+=1
    #         elif card.color=="BLUE":
    #             colors[1]+=1
    #         elif card.color=="GREEN":
    #             colors[2]+=1
    #         elif card.color=="YELLOW":
    #             colors[3]+=1
        
    #     maxIndex = np.argmax(colors)
    #     if maxIndex==0:
    #         return "RED"
    #     elif maxIndex==1:
    #         return "BLUE"
    #     elif maxIndex==2:
    #         return "GREEN"
    #     elif maxIndex==3:
    #         return "YELLOW"


    # def isWin(self):
    #     """ Returns True if the player has an empty hand (won the game) and false otherwise """
    #     return not self.hand

    # def displayHand(self):
    #     """ Returns a string containing all cards in the player's hand. """
    #     cards = ""
    #     for card in self.hand:
    #         cards += str(card)
    #     return cards

    # def __str__(self):
    #     """ Overridden toString() method displays AI's name and hand. """
    #     return str(self.name) + "'s hand: " + str(self.displayHand())
