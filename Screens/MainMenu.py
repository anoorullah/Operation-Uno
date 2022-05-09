import pygame, sys
from Components import Button, Message, Image
from Screens import PlayMenu, SettingsMenu
# from pygame import mixer as mix

class MainMenu():
    #def __init__(self, f_w, f_h, w, h, b_w, b_h, bg_color=pygame.Color("Purple")): # add sound boolean and variable for every cstr
    def __init__(self, w, h, bg_color=pygame.Color("Purple")): # add sound boolean and variable for every cstr

        """ Initializes the Main Menu with default size of 800x600 and a purple background """
        self.title = "Main Menu"
        # displayed screen dims
        self.w = w
        self.h = h
        self.bg_color = bg_color
        self.is_sound_on = True
        self.player_name = "Player Name"

    def setPlayerName(self, name):
        self.player_name = name

    def display(self):
        """ Displays the Main Menu and its components """
        # Initializes the main screen width and title
        main_menu = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption(self.title)
        
        # Determines the font size based on screen dimensions
        if self.w <= self.h:
            fontSize = self.w // 40
        else:
            fontSize = self.h // 20

        # Initialize text objects
        text_font = pygame.font.Font('Resources/Font/OpenSans-ExtraBold.ttf', fontSize*2)
        title_msg = Message.Message(main_menu, "OPERATION UNO", text_font, pygame.Color("White"), [self.w/2, self.h/8])

        # Initializes button colors and font
        red    = pygame.Color("Red")
        yellow = pygame.Color("Yellow")
        green  = pygame.Color("Green")
        blue   = pygame.Color("Blue")
        black  = pygame.Color("Black")
        button_font = pygame.font.Font('Resources/Font/OpenSans-Regular.ttf', fontSize)

        # Different buttons displayed on main menu
        play_button = Button.Button(main_menu, red, [self.w/4,self.h*3/4], [fontSize*5, fontSize*2.5], button_font, "Play", red, yellow)
        settings_button = Button.Button(main_menu, green, [self.w/2,self.h*3/4], [fontSize*7.5, fontSize*2.5], button_font, "Settings", green, yellow)
        quit_button = Button.Button(main_menu, blue, [self.w*3/4,self.h*3/4], [fontSize*5, fontSize*2.5], button_font, "Quit", blue, yellow)
        
        # pygame.mixer.init(48000, -16, 1, 1024)

        sound_img = Image.Image(main_menu, [self.w*8/9, self.h*8/9], [self.w/8, self.h/8], "Resources/Icons/SoundOn.png")
        uno_img = Image.Image(main_menu, [self.w/2, self.h/2.5], [self.w, self.h/4], "Resources/Icons/uno.png")

        while True:
            # Fills the screen with the background color
            main_menu.fill(self.bg_color)

            # if self.is_sound_on == True:
            #     menu_sound.play()
            # elif self.is_sound_on == False:
            #     menu_sound.stop()

            # Registers button presses and changes screens accordingly
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.isHovered():
                        play_button.play_sound()
                        play_menu = PlayMenu.PlayMenu(self.w, self.h)
                        play_menu.setPlayerName(self.player_name)
                        play_menu.display()
                        # print("Play button pressed")
                        # button_sound = pygame.mixer.Sound('Resources/Sounds/button-3.wav')
                        # button_sound.play()
                        # pygame.mixer.Channel(1).play(button_sound)
                        # pygame.display.quit() # Does this close window? --> Yes
                        # return
                    if settings_button.isHovered():
                        # button_sound = pygame.mixer.Sound('Resources/Sounds/button-3.wav')
                        # button_sound.play()
                        settings_menu = SettingsMenu.Settings(self.w, self.h)
                        settings_button.play_sound()
                        settings_menu.display()
                        self.player_name = settings_menu.getPlayerName()
                        # pygame.display.quit()
                        # return
                    if sound_img.isHovered():
                        # Logic for on/off with boolean
                        if self.is_sound_on == True:
                            sound_img.updateImage("Resources/Icons/SoundOff.png")
                            pygame.mixer.music.pause()
                            pygame.mixer.pause()
                        elif self.is_sound_on == False:
                            sound_img.updateImage("Resources/Icons/SoundOn.png")
                            pygame.mixer.music.unpause()
                            pygame.mixer.unpause()
                        # button_sound = pygame.mixer.Sound('Resources/Sounds/button-3.wav')
                        # pygame.mixer.Channel(2).play(button_sound)
                        # button_sound.play()
                        self.is_sound_on = not self.is_sound_on
                    if quit_button.isHovered():
                        # button_sound = pygame.mixer.Sound('Resources/Sounds/button-3.wav')
                        # pygame.mixer.Channel(2).play(button_sound)
                        print("Thanks for playing")
                        quit_button.play_sound()
                        pygame.quit()
                        sys.exit()

            # Displays the components of main menu
            title_msg.displayMessage()
            play_button.displayButton()
            settings_button.displayButton()
            quit_button.displayButton()
            sound_img.displayImage()
            uno_img.displayImage()

            # Refreshes the screen to update the changes
            pygame.display.update()
