import pygame
  
class ButtonSprite(pygame.sprite.Sprite):
    def __init__(self, screen, pos, dim, message, font, base_text_color, hover_text_color):
        super().__init__()

        self.screen = screen
        
        self.base_text = font.render(message, True, base_text_color)
        self.hover_text = font.render(message, True, hover_text_color)

        self.image = pygame.image.load("ButtonImage.png")
        self.image = pygame.transform.scale(self.image, dim)

        self.rect = self.image.get_rect(center=pos)
        self.text_rect = self.base_text.get_rect(center=pos, size=dim)

        self.click_sound = pygame.mixer.Sound("Resources/Sounds/ButtonClick.mp3")

    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.screen.blit(self.hover_text, self.text_rect)
        else:
            self.screen.blit(self.base_text, self.text_rect)
        
    def clicked(self):
        self.click_sound.play()
