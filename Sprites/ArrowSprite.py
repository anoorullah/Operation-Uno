import pygame
import numpy as np
from pygame.math import Vector2

class ArrowSprite(pygame.sprite.Sprite):
    def __init__(self, pos, dim, initial_angle):
        super().__init__()
        # pos = (center x, center y), dim = (width, height)

        self.pos = pos      # saves the position of the card

        # Loads in the image and scales the image to fit dim accordingly
        self.image = pygame.image.load("./Resources/Icons/Arrow.png")
        image_dim = self.image.get_size()
        image_scale = min(dim[0]/image_dim[0], dim[1]/image_dim[1])
        self.dim = tuple(i*image_scale for i in image_dim)
        self.image = pygame.transform.scale(self.image, self.dim)

        self.orig_image = self.image

        # Rectangle that bounds the image
        self.rect = self.image.get_rect(center=pos)

        self.curr_angle = initial_angle
        self.target_angle = initial_angle
        self.image = pygame.transform.rotozoom(self.orig_image, self.curr_angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.clockwise = True

        # Spin Arrow Sound
        # self.spin_sound = pygame.mixer.Sound("Resources/Sounds/PlaceCard.mp3")

    def update(self):
        """ Updates the position of the card to a place towards the new position """
        diff = (self.target_angle-self.curr_angle+180) % 360 - 180
        diff = diff+360 if diff<-180 else diff
        if abs(diff)>2:
            self.curr_angle = self.curr_angle-5 if self.clockwise else self.curr_angle+5
            if self.curr_angle < 0:
                self.curr_angle+=360
            self.curr_angle = self.curr_angle%360
            self.image = pygame.transform.rotozoom(self.orig_image, self.curr_angle, 1)
            self.rect = self.image.get_rect(center=self.rect.center)

    # def spin(self):
    #     """ Plays the placing card sound effect """
    #     self.spin_sound.play()

    def update_angle(self, angle):
        self.target_angle = angle

    def toggle_clockwise(self):
        self.clockwise = not self.clockwise
