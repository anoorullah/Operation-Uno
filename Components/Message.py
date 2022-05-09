import pygame

class Message():
    def __init__(self, window, msg, font, color, pos):
        """ Constructs a message that can be displayed. A message can have its text, font, color, pos, and target window customized. """
        self.msg = msg
        self.font = font
        self.color = color
        self.pos = pos
        self.window = window

    def displayMessage(self):
        """ Displays message to its target window. """
        text = self.font.render(self.msg, True, self.color)
        text_rect = text.get_rect(center=self.pos)
        self.window.blit(text, text_rect)

    def changeMessage(self, new_msg):
        """ Modifies a messages text. """
        self.msg = new_msg

    def changeColor(self, color):
        """ Modifies the color of a message. """
        self.color = color