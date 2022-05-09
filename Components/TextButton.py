import pygame

# black = pygame.Color("Black")
class TextButton:
    def __init__(self, window, color, pos, size, font, msg, base_color, hover_color, scale=1.1):
        """ Initializes a Text Button and sets each element of Button """
        self.color = color
        self.font = font
        self.msg = msg

        self.base_color = base_color
        self.hover_color = hover_color

        self.text = self.font.render(msg, True, pygame.Color("Black"))
        self.typed_text = self.font.render("", True, pygame.Color("Black"))

        self.typed_entry = ""
        self.temp_msg = ""
        self.temp_text = self.text

        self.window = window
        
        self.active = False
        self.new_text = False

        self.button_rect = pygame.Rect((pos[0]-size[0]//2, pos[1]-size[1]//2), size)
        self.text_rect = self.text.get_rect(center=pos, size=size)

    def displayButton(self):
        """ Handles displaying the text button on the screen """
        if self.isHovered():
            self.text = self.font.render(self.msg, True, pygame.Color("Black"))
            pygame.draw.rect(self.window, self.hover_color, self.button_rect, 0, 10)
        else:
            self.text = self.font.render(self.msg, True, pygame.Color("Black"))
            pygame.draw.rect(self.window, self.base_color, self.button_rect, 0, 10)

        self.window.blit(self.text, self.text_rect)

    def isHovered(self):
        """ Returns whether or not the cursor is hovering the text button """
        # Gets the mouse position
        mouse_pos = pygame.mouse.get_pos()
        return mouse_pos[0] in range(self.button_rect.left, self.button_rect.right) and mouse_pos[1] in range(self.button_rect.top, self.button_rect.bottom)

    def isClickedInBounds(self):
        """ Handles the typing and active logic of a text button when clicked in bounds """
        if not self.active and self.new_text:
            self.active = True
        elif not self.active:
            self.active = True
            self.new_text = True
            self.temp_text = self.text
            self.text = self.typed_text
            self.temp_msg = self.msg
            self.msg = self.typed_entry

    def isClickedOutBounds(self):
        """ Handles the typing and active logic of a text button when clicked out of bounds """
        if self.active and len(self.msg) == 0:
            self.active = False
            self.new_text = False
            self.text = self.temp_text
            self.msg = self.temp_msg
        if self.active:
            self.active = False

    def isActive(self):
        """ Returns status of whether the text button is currently selected """
        return self.active

    def hasNewText(self):
        """ Returns status of non-default text entry in text button """
        return self.new_text

    def backspace(self):
        """ Deletes one character from inputted text """
        if self.active:
            if len(self.msg) > 0:
                self.msg = self.msg[:-1]
    
    def write(self, char):
        """ Adds one character to inputted text """
        if self.active:
            if len(self.msg) < 9:
                self.msg += char

    def getText(self):
        """ Returns currently stored input text """
        return self.msg