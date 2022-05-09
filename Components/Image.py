import pygame

class Image:
    def __init__(self, window, pos, size, image_path):
        """ 
        Initializes the Image class. A card image requires:
            self.window - target window to be displayed on.
            self.base_pos - the original position decides the 'default' position of a image when it is not being dragged by a user. 
            self.pos - position of a image. Can be updated when 'dragging' the image.
            self.size - visual size of a image.
            self.clicked - click information necessary for 'dragging' functionality.
        """
        self.window = window
        self.base_pos = pos
        self.pos = pos
        self.size = size
        self.clicked = False

        png = pygame.image.load(image_path)
        png_dims = png.get_size()
        png_scale_factor = min(size[0]/png_dims[0], size[1]/png_dims[1])
        self.new_png_dims = tuple(i*png_scale_factor for i in png_dims)
        self.image = pygame.transform.scale(png, self.new_png_dims)
        self.image_rect = self.image.get_rect(center=pos, size=self.new_png_dims)

    def displayImage(self):
        """ Displays image to window. """
        if not self.clicked:
            self.pos = self.base_pos
        self.image_rect = self.image.get_rect(center=self.pos, size=self.new_png_dims)
        self.window.blit(self.image, self.image_rect)
    
    def isHovered(self):
        """ Returns status of mouse being hovered over card image. """
        mouse_pos = pygame.mouse.get_pos()
        return mouse_pos[0] in range(self.image_rect.left, self.image_rect.right) and mouse_pos[1] in range(self.image_rect.top, self.image_rect.bottom)

    def updateImage(self, image_path):
        """ Updates displayed PNG for image. """
        png = pygame.image.load(image_path)
        png_dims = png.get_size()
        png_scale_factor = min(self.size[0]/png_dims[0], self.size[1]/png_dims[1])
        self.new_png_dims = tuple(i*png_scale_factor for i in png_dims)
        self.image = pygame.transform.scale(png, self.new_png_dims)
        self.image_rect = self.image.get_rect(center=self.pos, size=self.new_png_dims)

    def updatePos(self, new_pos):
        """ Updates position for image. """
        if self.clicked:
            self.pos = new_pos