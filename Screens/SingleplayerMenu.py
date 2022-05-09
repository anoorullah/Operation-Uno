import pygame, sys
from Components import Button, Message
from Screens import PlayMenu, GameWindow
import Game
import Ruleset
import Deck

class SingleplayerMenu():
    def __init__(self, width=800, height=600, bg_color=pygame.Color("Purple")):
        """ Initializes the Main Menu with default size of 800x600 and a purple background """
        self.title = "Singleplayer Menu"
        self.w = width
        self.h = height
        self.bg_color = bg_color
        self.num_players = 1
        self.difficulty = "Easy"
        self.player_name = "Player Name"

    def setPlayerName(self, name):
        self.player_name = name

    def display(self):
        """ Displays the Main Menu and its components """
        # Initializes the main screen width and title
        singleplayer_menu = pygame.display.set_mode((self.w, self.h))
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
        num_players_text = Message.Message(singleplayer_menu, "NUMBER OF AI: 1", text_font, white, [self.w/2, self.h/8])
        difficulty_text = Message.Message(singleplayer_menu, "DIFFICULTY: Easy", text_font, white, [self.w/2, self.h/2])
        #png = pygame.image.load('Resources/Images/uno.png')
        #png_dims = png.get_size()

        # Initializes buttons
        button_font = pygame.font.Font('Resources/Font/OpenSans-Regular.ttf', fontSize)

        players_2 = Button.Button(singleplayer_menu, red, [self.w*1/4,self.h*5/16], [fontSize*2.5, fontSize*2.5], button_font, "1", red, yellow)
        players_3 = Button.Button(singleplayer_menu, green, [self.w*1/2,self.h*5/16], [fontSize*2.5, fontSize*2.5], button_font, "2", green, yellow)
        players_4 = Button.Button(singleplayer_menu, blue, [self.w*3/4,self.h*5/16], [fontSize*2.5, fontSize*2.5], button_font, "3", blue, yellow)
        player_buttons = [players_2, players_3, players_4]

        easy = Button.Button(singleplayer_menu, red, [self.w/4,self.h*11/16], [fontSize*5, fontSize*2.5], button_font, "Easy", red, yellow)
        medium = Button.Button(singleplayer_menu, green, [self.w/2,self.h*11/16], [fontSize*5, fontSize*2.5], button_font, "Medium", green, yellow)
        hard = Button.Button(singleplayer_menu, blue, [self.w*3/4,self.h*11/16], [fontSize*5, fontSize*2.5], button_font, "Hard", blue, yellow)
        difficulty_buttons = [easy, medium, hard]

        start_game_button = Button.Button(singleplayer_menu, blue, [self.w/2,self.h*7/8], [self.w/2, fontSize*2.5], button_font, "START", white, yellow)
        back_button = Button.Button(singleplayer_menu, blue, [self.w*7/8,self.h*7/8], [fontSize*5, fontSize*2.5], button_font, "Back", white, yellow)

        # Initialize Ruleset/Cardset
        # cardset = Deck.Deck/()
        # ruleset = Ruleset.Ruleset()
        
        current = True
        while current:
            # Fills the screen with the background color
            singleplayer_menu.fill(self.bg_color)

            # Registers button presses and changes screens accordingly
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Number of Players buttons
                    for button in player_buttons:
                        if button.isHovered():
                            button.play_sound()
                            self.num_players = int(button.msg)
                            num_players_text.changeMessage("NUMBER OF AI: " + str(self.num_players))
                    
                    # Difficulty buttons
                    for button in difficulty_buttons:
                        if button.isHovered():
                            button.play_sound()
                            self.difficulty = button.msg
                            difficulty_text.changeMessage("DIFFICULTY: " + self.difficulty)

                    if start_game_button.isHovered():
                        start_game_button.play_sound()
                        game_instance = Game.Game(self.w, self.h, False, self.num_players, self.difficulty)
                        game_instance.setMainPlayerName(self.player_name)
                        game_window = GameWindow.GameWindow(game_instance, self.w, self.h)
                        game_window.display()
                        pygame.display.quit()
                        return
                        
                    if back_button.isHovered():
                        back_button.play_sound()
                        play_menu = PlayMenu.PlayMenu(self.w, self.h)
                        play_menu.setPlayerName(self.player_name)
                        play_menu.display()
                        pygame.display.quit()
                        return

            # Displays the components of main menu
            num_players_text.displayMessage()
            difficulty_text.displayMessage()

            for button in player_buttons:
                button.displayButton()
            for button in difficulty_buttons:
                button.displayButton()
            start_game_button.displayButton()
            back_button.displayButton()
            
            # Refreshes the screen to update the changes
            pygame.display.update()
