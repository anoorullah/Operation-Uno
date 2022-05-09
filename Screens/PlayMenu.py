import pygame, sys
from Components import Button, Message
from Screens import MainMenu, SingleplayerMenu, MultiplayerMenu

class PlayMenu():
    def __init__(self, width=800, height=600, bg_color=pygame.Color("Purple")):
        """ Initializes the Main Menu with default size of 800x600 and a purple background """
        self.title = "Play Menu"
        self.w = width
        self.h = height
        self.bg_color = bg_color
        self.player_name = "Player Name"

    def setPlayerName(self, name):
        self.player_name = name

    def display(self):
        """ Displays the Main Menu and its components """
        # Initializes the main screen width and title
        play_menu = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption(self.title)
        
        # Determines the font size based on screen dimensions
        if self.w <= self.h:
            fontSize = self.w // 50
        else:
            fontSize = self.h // 20

        # Initialize colors
        red    = pygame.Color("Red")
        yellow = pygame.Color("Yellow")
        green  = pygame.Color("Green")
        blue   = pygame.Color("Blue")
        white  = pygame.Color("White")

        # Initialize text objects
        text_font = pygame.font.Font('Resources/Font/OpenSans-ExtraBold.ttf', fontSize*2)
        player_mode = Message.Message(play_menu, "CHOOSE YOUR MODE", text_font, white, [self.w/2, self.h/4])
        #png = pygame.image.load('Resources/Images/uno.png')
        #png_dims = png.get_size()

        # Initializes buttons
        button_font = pygame.font.Font('Resources/Font/OpenSans-Regular.ttf', fontSize)

        singleplayer_button = Button.Button(play_menu, blue, [self.w/2,self.h/2], [self.w/1.5, fontSize*2.5], button_font, "Singleplayer", white, yellow)
        # multiplayer_button = Button.Button(play_menu, blue, [self.w/2,self.h*3/4], [self.w/2, fontSize*2.5], button_font, "Multiplayer", white, yellow)
        back_button = Button.Button(play_menu, blue, [self.w*7/8,self.h*7/8], [fontSize*5, fontSize*2.5], button_font, "Back", white, yellow)

        while True:
            # Fills the screen with the background color
            play_menu.fill(self.bg_color)

            # Registers button presses and changes screens accordingly
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if singleplayer_button.isHovered():
                        singleplayer_button.play_sound()
                        singleplayer_menu = SingleplayerMenu.SingleplayerMenu(self.w, self.h)
                        singleplayer_menu.setPlayerName(self.player_name)
                        singleplayer_menu.display()
                        pygame.display.quit()
                        return

                    # if multiplayer_button.isHovered():
                    #     multiplayer_menu = MultiplayerMenu.MultiplayerMenu(self.w, self.h)
                    #     multiplayer_menu.display()
                    #     pygame.display.quit()
                    #     return

                    elif back_button.isHovered():
                        back_button.play_sound()
                        main_menu = MainMenu.MainMenu(self.w, self.h)
                        main_menu.setPlayerName(self.player_name)
                        main_menu.display()
                        pygame.display.quit()
                        return

            # Displays the components of main menu
            player_mode.displayMessage()

            singleplayer_button.displayButton()
            # multiplayer_button.displayButton()
            back_button.displayButton()
            
            # Refreshes the screen to update the changes
            pygame.display.update()
