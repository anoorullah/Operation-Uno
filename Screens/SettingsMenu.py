import pygame, sys
from Components import Button, Message, TextButton
from Screens import MainMenu, PlayMenu

class Settings():
    def __init__(self, width=800, height=600, bg_color=pygame.Color("Purple")):
        """ Initializes the Main Menu with default size of 800x600 and a Purple background """
        self.title = "Settings"
        self.w = width
        self.h = height
        self.bg_color = bg_color
        self.accounts = []
        self.lines = []
        self.num_accounts = 0
        self.account_map = {}
        self.loadAccounts()
        self.parseAccounts()
        self.player_name = "Player Name"
        #testing
        # for account in self.lines:
        #     print(account)

    def loadAccounts(self):
        """ Loads accounts from storage text file """
        with open('Accounts.txt','r') as f:
            self.lines = f.readlines()
        self.num_accounts = len(self.lines)

    def parseAccounts(self):
        """ Formats loaded account data into username/password format for dictionary """
        for line in self.lines:
            username = ""
            password = ""
            pass_flag = False
            for i in range(len(line)):
                if line[i] == ';' or line[i] == " " or line[i] == "\n":
                    pass_flag = True
                    continue
                if not pass_flag:
                    username += line[i]
                else:
                    password += line[i]
            self.account_map[username] = password

    def encodeAccount(self, username, password):
        """ Encodes account for future storing """
        account = "\n" + username + "; " + password
        return account

    def updateAccounts(self):
        """ Updates account storage file """
        with open('Accounts.txt', 'a') as f:
            for i in range(self.num_accounts, len(self.lines)):
                f.write(self.lines[i])

    def register(self, username, password):
        """ Handles register logic of an account. Returns true if successful, false otherwise """
        if username in self.account_map:
            return False
        else:
            account = self.encodeAccount(username, password)
            self.lines.append(account)
            self.account_map[username] = password
            return True

    def login(self, username, password):
        """ Handles login logic of an account. Returns true if successful, false otherwise """
        if username in self.account_map and self.account_map[username] == password:
            #login as player name **********TODO******************
            self.player_name = username
            return True
        else:
            return False

    def getPlayerName(self):
        return self.player_name
        
    def display(self):
        """ Displays the Settings Menu and its components """
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
        error_font = pygame.font.Font('Resources/Font/OpenSans-ExtraBold.ttf', fontSize//2)

        # Initializes button colors
        red    = pygame.Color("Red")
        yellow = pygame.Color("Yellow")
        green  = pygame.Color("Green")
        blue   = pygame.Color("Blue")
        white = pygame.Color("White")
        button_font = pygame.font.Font('Resources/Font/OpenSans-Regular.ttf', fontSize)

        account_msg = Message.Message(main_menu, "Account Settings", text_font, pygame.Color("Black"), [self.w/2, self.h/8])
        username_text_btn = TextButton.TextButton(main_menu, white, [self.w/4,self.h/2], [fontSize*7.5, fontSize*2.25], button_font, "Username", white, pygame.Color("Gray"))
        password_text_btn = TextButton.TextButton(main_menu, white, [self.w/4,self.h/2 + 120], [fontSize*7.5, fontSize*2.25], button_font, "Password", white, pygame.Color("Gray"))
        register_btn = Button.Button(main_menu, green, [self.w*3/4,self.h/2], [fontSize*5, fontSize*2.5], button_font, "Register", green, yellow)
        login_btn = Button.Button(main_menu, blue, [self.w*3/4,self.h/2 + 120], [fontSize*5, fontSize*2.5], button_font, "Login", blue, yellow)
        quit_button = Button.Button(main_menu, red, [self.w/2,self.h*3/4 + 80], [fontSize*5, fontSize*2.5], button_font, "Back", red, yellow)

        invalid_reg_msg = Message.Message(main_menu, "Invalid Registration", error_font, pygame.Color("Red"), [self.w/2, self.h/8 + 80])
        invalid_login_msg = Message.Message(main_menu, "Invalid Login", error_font, pygame.Color("Red"), [self.w/2, self.h/8 + 80])
        
        valid_reg_msg = Message.Message(main_menu, "Registration Succesful!", error_font, pygame.Color("Green"), [self.w/2, self.h/8 + 80])
        valid_login_msg = Message.Message(main_menu, "Login Succesful!", error_font, pygame.Color("Green"), [self.w/2, self.h/8 + 80])

        invalid_register = False
        invalid_login = False

        valid_register = False
        valid_login = False

        current = True
        while current:
            # Fills the screen with the background color
            main_menu.fill(self.bg_color)

            # Registers button presses and changes screens accordingly
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if username_text_btn.isHovered():
                        username_text_btn.isClickedInBounds()
                    else:
                        username_text_btn.isClickedOutBounds()
                    if password_text_btn.isHovered():
                        password_text_btn.isClickedInBounds()
                    else:
                        password_text_btn.isClickedOutBounds()
                    if register_btn.isHovered():
                        if username_text_btn.hasNewText() and password_text_btn.hasNewText():
                            if self.register(username_text_btn.getText(), password_text_btn.getText()):
                                invalid_register = False
                                invalid_login = False

                                valid_login = False
                                valid_register = True
                            else:
                                invalid_register = True
                                invalid_login = False

                                valid_login = False
                                valid_register = False
                        else:
                            invalid_login = False
                            invalid_register = True

                            valid_login = False
                            valid_register = False 
                    if login_btn.isHovered():
                        if username_text_btn.hasNewText() and password_text_btn.hasNewText():
                            if self.login(username_text_btn.getText(), password_text_btn.getText()):
                                invalid_register = False
                                invalid_login = False

                                valid_register = False
                                valid_login = True
                            else:
                                invalid_register = False
                                invalid_login = True

                                valid_register = False
                                valid_login = False
                        else:
                            invalid_register = False
                            invalid_login = True

                            valid_login = False
                            valid_register = False 
                    if quit_button.isHovered():
                        self.updateAccounts()
                        current = False
                elif event.type == pygame.KEYDOWN:
                    if username_text_btn.isActive():
                        if event.key == pygame.K_BACKSPACE:
                            username_text_btn.backspace() 
                        else:
                            username_text_btn.write(event.unicode) 
                    if password_text_btn.isActive():
                        if event.key == pygame.K_BACKSPACE:
                            password_text_btn.backspace() 
                        else:
                            password_text_btn.write(event.unicode) 
            
            # Displays the components of settings menu
            account_msg.displayMessage()
            username_text_btn.displayButton()
            password_text_btn.displayButton()
            register_btn.displayButton()
            login_btn.displayButton()
            quit_button.displayButton()

            if invalid_login:
                invalid_login_msg.displayMessage()
            if invalid_register:
                invalid_reg_msg.displayMessage()
            if valid_login:
                valid_login_msg.displayMessage()
            if valid_register:
                valid_reg_msg.displayMessage()
            pygame.display.update()
            # Refreshes the screen to update the changes