import pygame
import numpy as np

class CardSprite(pygame.sprite.Sprite):
    def __init__(self, pos, dim, card):
        super().__init__()

        # pos = (center x, center y), dim = (width, height)
        self.pos = pos
        self.initial_pos = pos

        self.card = card    # the actual Card object

        # Loads in the image and scales the image to fit dim accordingly
        self.front = pygame.image.load("Resources/Cards/" + str(card) + ".png")
        self.back = pygame.image.load("Resources/Cards/Back-of-card.png")
        image_dim = self.front.get_size()
        image_scale = min(dim[0]/image_dim[0], dim[1]/image_dim[1])
        self.dim = tuple(i*image_scale for i in image_dim)
        
        # Initialize front and back card images
        self.front = pygame.transform.scale(self.front, self.dim)
        self.back = pygame.transform.scale(self.back, self.dim)

        self.is_selected = False    # Indicates whether the card is currently hovered by cursor

        self.image = self.back      # Initially the card is not shown (except for the main player)
        
        # Rectangle that bounds the image
        self.rect = self.image.get_rect(center=pos)
    
        # Place Card Sound
        pygame.mixer.init()
        self.place_sound = pygame.mixer.Sound("Resources/Sounds/PlaceCard.wav")

    def update(self, is_placing, should_rotate):
        """ Updates the position of the card to a place towards the new position """
        # Parameters:
        #   - is_placing indicates whether the place card sound should be played
        #   - should_rotate is True when we want the card to rotate when placed in the middle
        curr_x = self.rect.centerx
        curr_y = self.rect.centery

        # Determines the change needed based on the distance of the card to its new position
        delta_x = (self.pos[0]-self.initial_pos[0])*self.distance(self.pos, self.rect.center)/5000
        delta_y = (self.pos[1]-self.initial_pos[1])*self.distance(self.pos, self.rect.center)/5000

        # Returns if the card is where it should be
        if(self.initial_pos[0]==self.pos[0] and self.initial_pos[1]==self.pos[1]):
            return

        # If the card is near its expected position, update the card to the new position
        if (delta_x > 0 and curr_x > self.pos[0] or delta_x < 0 and curr_x < self.pos[0] or abs(delta_x)<=5) and (delta_y > 0 and curr_y > self.pos[1] or delta_y < 0 and curr_y < self.pos[1] or abs(delta_y)<=5):
            self.rect.center = self.pos
            self.initial_pos = self.pos
            if is_placing:
                self.place()
            if should_rotate:
                self.image = pygame.transform.rotozoom(self.image, np.random.rand()*60-30, 1)
                self.rect = self.image.get_rect(center=self.rect.center)
            return

        # Otherwise move the card by the delta values
        self.rect.centerx += delta_x
        self.rect.centery += delta_y

    def distance(self, pos1, pos2):
        """ Returns the euclidian distance between the current position and the new position """
        return ((pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2)**0.5

    def place(self):
        """ Plays the placing card sound effect """
        self.place_sound.play()

    def update_card(self, new_card, replace_image):
        """ Updates the current card with a new card and updates the image """ 
        # Parameter replace_image is for updating the card color when player plays a wild card
        self.card = new_card
        self.front = pygame.image.load("Resources/Cards/" + str(new_card) + ".png")
        self.front = pygame.transform.scale(self.front, self.dim)
        if replace_image:
            self.image = self.front

    def update_pos(self, new_pos):
        """ Updates the new destinatiopn of the card """
        self.pos = new_pos
        # self.rect = self.image.get_rect(center=self.pos)

    def toggle_face(self):
        """ Toggles between showing the front and back of the card """
        self.image = self.front if self.image==self.back else self.back

    def __str__(self):
        """ Overridden toString() method displays the card. """
        return str(self.card.color) + " " + str(self.card.value)