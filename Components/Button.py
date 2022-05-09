import pygame

class Button:    
    def __init__(self, window, color, pos, size, font, msg, base_color, hover_color, scale=1.1):
        """ Initializes a Button and sets each element of Button """
        self.color = color
        self.font = font
        self.msg = msg
        self.base_color = base_color
        self.hover_color = hover_color
        self.text = self.font.render(msg, True, base_color)
        self.window = window

        self.base_text_rect = self.text.get_rect(center=pos, size=size)
        self.base_button_rect = self.text.get_rect(topleft=[pos[0]-size[0]//2, pos[1]-size[1]//2], size=size)
        
        scaleSize = tuple(i*scale for i in size)
        self.scale_text_rect = self.text.get_rect(center=pos, size=scaleSize)
        self.scale_button_rect = self.text.get_rect(topleft=[pos[0]-scaleSize[0]//2, pos[1]-scaleSize[1]//2], size=scaleSize)

        self.text_rect = self.base_text_rect
        self.button_rect = self.base_button_rect

        pygame.mixer.init()
        self.click_sound = pygame.mixer.Sound("Resources/Sounds/ButtonClick.wav")


    def displayButton(self):
        """ Handles displaying the button on the screen """
        if self.isHovered():
            self.text_rect = self.scale_text_rect
            self.button_rect = self.scale_button_rect
            self.text = self.font.render(self.msg, True, self.hover_color)
            pygame.draw.rect(self.window, self.hover_color, self.button_rect, 2, 10)
        else:
            self.text_rect = self.base_text_rect
            self.button_rect = self.base_button_rect
            self.text = self.font.render(self.msg, True, self.base_color)
            pygame.draw.rect(self.window, self.base_color, self.button_rect, 2, 10)
        
        self.window.blit(self.text, self.text_rect)
    
    def isHovered(self):
        """ Returns whether or not the cursor is hovering the button """
        # Gets the mouse position
        mouse_pos = pygame.mouse.get_pos()
        return mouse_pos[0] in range(self.button_rect.left, self.button_rect.right) and mouse_pos[1] in range(self.button_rect.top, self.button_rect.bottom)

    def play_sound(self):
        self.click_sound.play()