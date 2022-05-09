from Components import Button, Message, Image
from Sprites.CardSprite import CardSprite
from Sprites.ArrowSprite import ArrowSprite
from Screens import EndMenu
from Card import Card
from Game import Game
import pygame, sys
from time import time
import numpy as np

class GameWindow:
    def __init__(self, game_instance, width=800, height=600, bg_color=pygame.Color("Purple")):
        """ Initializes a game window to display a game. """
        self.title = "UNO Game"
        self.game_instance = game_instance
        self.w = width
        self.h = height
        self.bg_color = bg_color

    def update_cards(self, player, base_card_pos, selected_card):
        """ Updates the position of the cards in player's hand """
        num_cards = len(player.hand)
        card_offsets = np.linspace(-num_cards/2, num_cards/2, num_cards)
        i = 0
        if base_card_pos[0] == self.w/2: # top or bottom of screen
            for card in player.hand:
                if card==selected_card:
                    selected_card.update_pos((base_card_pos[0]+self.w*card_offsets[i]/32, base_card_pos[1]-self.h/64))
                else:
                    card.update_pos((base_card_pos[0]+self.w*card_offsets[i]/32, base_card_pos[1]))
                i+=1
        else:
            for card in player.hand:
                card.update_pos((base_card_pos[0], base_card_pos[1]+self.h*card_offsets[i]/32))
                i+=1

    def update_graphics(self, game_window):
        """ Updates the graphics of the game """
        # Draws the background
        game_window.fill(self.bg_color)

        curr_player = self.game_instance.getCurrPlayer()
        curr_player_idx = self.index_dict[curr_player]
        # Update the arrow to point to the current player
        self.arrow_sprite.update_angle(self.arrow_angles[curr_player_idx])

        # Draws the arrow
        self.arrow.draw(game_window)
        self.arrow.update()

        # Displays the cards that have been played
        self.game_instance.played_cards.draw(game_window)
        self.game_instance.played_cards.update(True, True)

        # Displays every players' hand
        for player in self.game_instance.players:
            player.hand.draw(game_window)
            player.hand.update(False, False)

        # Displays the draw and skip button
        if self.can_draw:
            self.draw_button.displayButton()
        else:
            self.skip_button.displayButton()

        if self.choose_color:
            for button in self.choose_color_buttons:
                button.displayButton()

        # Displays text labels
        self.turn_num_label.changeMessage("Turn Number: " + str(self.game_instance.actual_turn))
        self.curr_player_label.changeMessage("Current Player: " + str(curr_player.name))
        self.turn_num_label.displayMessage()
        self.curr_player_label.displayMessage()

        pygame.display.flip()
        self.clock.tick(60)

    def initialize_player_positions(self, num_players):
        """ Initialize the positions and arrow angles of each player on the board """
        # Positions of the players' hands on the screen
        card_positions = []
        bottom = (self.w/2, self.h*7/8)
        left = (self.w/8, self.h/2)
        top = (self.w/2, self.h*1/8)
        right = (self.w*7/8, self.h/2)
        card_positions.append(bottom)
        if num_players==2:
            card_positions.append(top)
        if num_players==3:
            card_positions.append(left)
            card_positions.append(right)
        if num_players==4:
            card_positions.append(left)
            card_positions.append(top)
            card_positions.append(right)

        # Arrow angle positions of the players
        arrow_angles = []
        if self.num_players==2:
            arrow_angles.append(0)
            arrow_angles.append(180)
        if self.num_players==3:
            arrow_angles.append(0)
            arrow_angles.append(-90)
            arrow_angles.append(90)
        if self.num_players==4:
            arrow_angles.append(0)
            arrow_angles.append(-90)
            arrow_angles.append(180)
            arrow_angles.append(90)

        return card_positions, arrow_angles

    def update_next_turn(self, events, mouse_pos):
        """ Handles updating the next turn if its AI or player """
        curr_player = self.game_instance.getCurrPlayer()

        # Updates the AI's next turn
        if curr_player.isAI:
            if self.game_instance.update_turn(curr_player):
                self.arrow_sprite.toggle_clockwise()
            return True

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # DRAW BUTTON LOGIC
                if self.draw_button.isHovered() and self.can_draw:
                    self.draw_button.play_sound()
                    self.game_instance.draw(self.game_instance.main_player, 1)
                    self.can_draw = False
                    self.mouse_down = True
                    # print("Main player drew")
                    return True
                # SKIP BUTTON LOGIC
                elif self.skip_button.isHovered() and not self.can_draw and not self.mouse_down:
                    self.skip_button.play_sound()
                    self.game_instance.skipTurn()
                    self.can_draw = True
                    # print("Main player skipped turn")
                    return True

                # If needs to choose a color
                if self.choose_color:
                    for button in self.choose_color_buttons:
                        if button.isHovered():
                            button.play_sound()
                            self.temp_wild_card.update_card(Card(button.msg, self.temp_wild_card.card.value), True)
                            if self.game_instance.update_turn(self.game_instance.main_player, self.temp_wild_card):
                                self.arrow_sprite.toggle_clockwise()
                            self.can_draw = True
                            return True

                # MAIN PLAYER LOGIC
                if self.selected_card:
                    # If selected card is a wild card, toggle choosing a color
                    if self.selected_card.card.color == "WILD":
                        self.choose_color = True
                        self.temp_wild_card = self.selected_card
                        return False
                    elif self.game_instance.ruleset.isValid(self.selected_card, self.game_instance.top_card):
                        if self.game_instance.update_turn(self.game_instance.main_player, self.selected_card):
                            self.arrow_sprite.toggle_clockwise()
                        self.can_draw = True
                        return True
        return False

    def display(self):
        """ Displays the game window and allows for a game to be played using the logic of the imported components. """
        self.clock = pygame.time.Clock()
        self.last_time = time()

        game_window = pygame.display.set_mode((self.w, self.h))

        self.num_players = self.game_instance.total_players
        self.card_positions, self.arrow_angles = self.initialize_player_positions(self.num_players)

        # Initialize the player and their respective indices and vice versa
        index = self.game_instance.players.index(self.game_instance.main_player)
        player_dict = {}
        self.index_dict = {}
        for i in range(self.num_players):
            player_dict[i] = self.game_instance.players[(index+i)%(self.num_players)]
            self.index_dict[self.game_instance.players[(index+i)%(self.num_players)]] = i
        
        # VARIABLES
        self.can_draw       = True  # Toggle between drawing and skipping turn
        self.mouse_down     = False # Toggle that checks if the mouse is held down and not lifted
        self.selected_card  = None  # The current card in player's hand that is hovered by cursor
        self.temp_wild_card = None  # Set to selected card when a wild card was clicked
        self.paused         = True  # Toggles whether the game is paused (no moves made)
        self.choose_color   = False # True when player needs to choose a color

        # Update the positions of the cards to their players' hands
        for i in range(self.num_players):
            self.update_cards(player_dict[i], self.card_positions[i], self.selected_card)

        # Update the position of the top card
        self.game_instance.top_card.toggle_face()
        self.game_instance.top_card.update_pos((self.w/2, self.h/2))
        
        # Point the arrow to the current player
        curr_player_idx = self.index_dict[self.game_instance.getCurrPlayer()]
        self.arrow_sprite = ArrowSprite((self.w/2, self.h/2), (self.w/2.5, self.h/2.5), self.arrow_angles[curr_player_idx])
        self.arrow = pygame.sprite.Group(self.arrow_sprite)

        # COLORS
        red    = pygame.Color("Red")
        yellow = pygame.Color("Yellow")
        green  = pygame.Color("Green")
        blue   = pygame.Color("Blue")
        white  = pygame.Color("White")
        black  = pygame.Color("Black")

        # BUTTONS!
        fontSize = self.w // 50 if self.w <= self.h else self.h // 20
        button_font = pygame.font.Font('Resources/Font/OpenSans-Regular.ttf', fontSize)

        self.draw_button = Button.Button(game_window, red, [self.w*7/8, self.h*7/8], [fontSize*4, fontSize*2], button_font, "Draw", red, yellow)
        self.skip_button = Button.Button(game_window, red, [self.w*7/8, self.h*7/8], [fontSize*4, fontSize*2], button_font, "Skip", red, yellow)
        
        color_button_font = pygame.font.Font('Resources/Font/OpenSans-Regular.ttf', fontSize//2)
        r_button = Button.Button(game_window, red, [self.w*13/32, self.h*3/4], [fontSize*2, fontSize*1], color_button_font, "RED", red, red)
        y_button = Button.Button(game_window, yellow, [self.w*15/32, self.h*3/4], [fontSize*2, fontSize*1], color_button_font, "YELLOW", yellow, yellow)
        g_button = Button.Button(game_window, green, [self.w*17/32, self.h*3/4], [fontSize*2, fontSize*1], color_button_font, "GREEN", green, green)
        b_button = Button.Button(game_window, blue, [self.w*19/32, self.h*3/4], [fontSize*2, fontSize*1], color_button_font, "BLUE", blue, blue)
        self.choose_color_buttons = [r_button, y_button, g_button, b_button]

        # TEXT LABELS
        text_font = pygame.font.Font('Resources/Font/OpenSans-ExtraBold.ttf', int(fontSize/2))
        self.turn_num_label = Message.Message(game_window, "Turn Number: ", text_font, black, [self.w/8, self.h*6/8])
        self.curr_player_label = Message.Message(game_window, "Current Player: ", text_font, black, [self.w/8, self.h*7/8])

        # Main game loop
        while not self.game_instance.get_winner():
            mouse_pos = pygame.mouse.get_pos()
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_down = False

            if not self.selected_card:
                for card in self.game_instance.main_player.hand:
                    if card.rect.collidepoint(mouse_pos):
                        self.selected_card = card
                        self.selected_card.is_selected = True
            elif self.selected_card:
                if not self.selected_card.rect.collidepoint(mouse_pos):
                    self.selected_card.is_selected = False
                    self.selected_card = None

            if self.paused:
                if time()-self.last_time > 2:
                    self.last_time = time()
                    self.paused = False         
            elif not self.paused:
                if self.update_next_turn(events, mouse_pos):
                    self.choose_color = False
                    if self.game_instance.getCurrPlayer().isAI:
                        self.paused = True
                        self.last_time = time()

            for i in range(self.num_players):
                self.update_cards(player_dict[i], self.card_positions[i], self.selected_card)

            self.update_graphics(game_window)

        print(self.game_instance.get_winner().name)
        end_menu = EndMenu.EndMenu(self.game_instance.getMainPlayerName(), self.game_instance.get_winner().name, self.w, self.h)
        end_menu.display()

        pygame.display.quit()
        return