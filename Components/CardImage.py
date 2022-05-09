import pygame

class CardImage:
    def __init__(self, window, pos, size, card):
        """ 
        Initializes the CardImage class. A card image requires:
            self.window - target window to be displayed on.
            self.base_pos - the original position decides the 'default' position of a card when it is not being dragged by a user. 
            self.pos - position of a card image. Can be updated when 'dragging' a card.
            self.size - visual size of a card image.
            self.clicked - click information necessary for 'dragging' functionality.
            self.card - the corresponding card to be displayed visually.
        """
        self.window = window
        self.base_pos = pos
        self.pos = pos
        self.size = size
        self.clicked = False
        self.card = card

        self.png = pygame.image.load("Resources/Cards/" + str(card) + ".png")
        png_dims = self.png.get_size()
        png_scale_factor = min(size[0]/png_dims[0], size[1]/png_dims[1])
        self.new_png_dims = tuple(i*png_scale_factor for i in png_dims)
        self.image = pygame.transform.scale(self.png, self.new_png_dims)
        self.image_rect = self.image.get_rect(center=pos, size=self.new_png_dims)

    def displayImage(self):
        """ Displays card image based on its 'dragging' status. """
        if not self.clicked:
            self.pos = self.base_pos
        self.image_rect = self.image.get_rect(center=self.pos, size=self.new_png_dims)
        self.window.blit(self.image, self.image_rect)

    def isHovered(self):
        """ Returns status of mouse being hovered over card image. """
        mouse_pos = pygame.mouse.get_pos()
        return mouse_pos[0] in range(self.image_rect.left, self.image_rect.right) and mouse_pos[1] in range(self.image_rect.top, self.image_rect.bottom)

    def checkInBounds(self, bounds):
        """ Returns status of mouse being hovered over passed in bounds. """
        mouse_pos = pygame.mouse.get_pos()
        #return mouse_pos[0] in range(bounds[0][0], bounds[1][0]) and mouse_pos[1] in range(bounds[0][1], bounds[1][1])
        return mouse_pos[0] in range(bounds.left, bounds.right) and mouse_pos[1] in range(bounds.top, bounds.bottom)

    def updateImage(self, image_path):
        """ Updates displayed PNG for card image. """
        png = pygame.image.load(image_path)
        png_dims = png.get_size()
        png_scale_factor = min(self.size[0]/png_dims[0], self.size[1]/png_dims[1])
        self.new_png_dims = tuple(i*png_scale_factor for i in png_dims)
        self.image = pygame.transform.scale(png, self.new_png_dims)
        self.image_rect = self.image.get_rect(center=self.pos, size=self.new_png_dims)

    def updatePos(self, new_pos):
        """ Updates real-time position of card image. """
        if self.clicked:
            self.pos = new_pos

    def updateBasePos(self, new_pos):
        """ Updates 'default' position of card image. """
        self.base_pos = new_pos
    
    def updateCard(self, new_card):
        '''Updating Top Card'''
        self.card = new_card
        self.png = pygame.image.load("Resources/Cards/" + str(self.card) + ".png")
        self.image = pygame.transform.scale(self.png, self.new_png_dims)
    # def updateSize(self, new_size): not sure if needed

    def animateMove(self, base_pos, new_pos):
        while base_pos!=new_pos:
            self.updateBasePos((new_pos-base_pos)/computeDist(base_pos, new_pos))
            self.displayImage()
        self.updateBasePos(new_pos)
        self.displayImage()

    def computeDist(self, pos1, pos2):
        return (pos1[0]-pos2[0])*(pos1[1]-pos2[1]) + (pos1[1]-pos2[1])*(pos1[1]-pos2[1])