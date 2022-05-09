from Components import Button, Message, Image, CardImage
from Game import Game
import pygame, sys
from time import sleep, time
import numpy as np
from pygame import mixer as mix

def updateCards(self, player, base_card_pos, window):
    """ Updates the visual display of all cards on the screen that are currently in players hands. """
    num_cards = len(player.hand)
    card_offsets = np.linspace(-num_cards/2, num_cards/2, num_cards)
    if base_card_pos[0] == self.w/2: # top or bottom of screen
        for i in range(num_cards):
            self.card_imgs.append(CardImage.CardImage(window, [base_card_pos[0]+self.w*card_offsets[i]/32, base_card_pos[1]], [self.w/8, self.h/8], player.hand[i]))
    else:
        for i in range(num_cards):
            self.card_imgs.append(CardImage.CardImage(window, [base_card_pos[0], base_card_pos[1]+self.h*card_offsets[i]/32], [self.w/8, self.h/8], player.hand[i]))


'''
import threading 

def ai_play(): 
    print("2 seconds finished") 

timer = threading.Timer(2.0, func)
timer.start()'''

class GameWindow_decommisioned:
    def __init__(self, game_instance, width=800, height=600, bg_color=pygame.Color("Purple")):
        """ Initializes a game window to display a game. """
        self.title = "UNO Game"
        self.game_instance = game_instance
        self.w = width
        self.h = height
        self.bg_color = bg_color
        self.card_imgs = []
        self.middle_bound = pygame.Rect((self.w / 2 - self.w / 8, self.h / 2 - self.h / 8), (self.w / 4, self.h / 4))
        #self.draw_button
    def showWinScreen(self, winningPlayer, game_window, you_win_label):
        winningPlayer = self.game_instance.getWinner()
        if not winningPlayer.isAI: # What happens if main player wins
            win_sound = mix.Sound('Resources/Sounds/Fanfare-sound.wav')
            win_sound.set_volume(0.5)
            win_sound.play()
            game_window.fill(pygame.Color("Black"))
            you_win_label.displayMessage()
        else: # What happens if one of the AI players wins
            lose_sound = mix.Sound('Resources/Sounds/Fanfare-sound.wav')
            lose_sound.set_volume(0.5)
            lose_sound.play()
            game_window.fill(pygame.Color("Black"))
            you_win_label.displayMessage()

    def display(self):
        """ Displays the game window and allows for a game to be played using the logic of the imported components. """
        clock = pygame.time.Clock()
        game_window = pygame.display.set_mode((self.w, self.h))
        self.top_card = CardImage.CardImage(game_window, [self.w/2, self.h/2], [self.w/8, self.h/8], self.game_instance.top_card)


        # Determines the font size based on screen dimensions
        if self.w <= self.h:
            fontSize = self.w // 50
        else:
            fontSize = self.h // 20

        #Initialize colors
        red    = pygame.Color("Red")
        yellow = pygame.Color("Yellow")
        green  = pygame.Color("Green")
        blue   = pygame.Color("Blue")
        white  = pygame.Color("White")
        black = pygame.Color("Black")

        # Initialize text objects
        text_font = pygame.font.Font('Resources/Font/OpenSans-ExtraBold.ttf', int(fontSize/2))
        large_text = pygame.font.Font('Resources/Font/OpenSans-ExtraBold.ttf', int(fontSize * 2))
        # num_turns_label = Message.Message(game_window, "Turn Number", text_font, black, [100, 100])
        # num_turns = Message.Message(game_window, "", large_text, black, [100, 200])
        # current_player_label = Message.Message(game_window, "Current player", text_font, black, [100, 300])
        # current_player = Message.Message(game_window, "", text_font, black, [100, 400])

        labels = [num_turns_label, num_turns, current_player_label, current_player]
        num_turns_label = Message.Message(game_window, "Number of turns: ", text_font, black, [100, 100])
        current_player_label = Message.Message(game_window, "Current player: ", large_text, black, [400, self.h - 550])
        num_turns = Message.Message(game_window, "0", text_font, black, [200, 100])
        #current_player = Message.Message(game_window, "0", large_text, black, [1000, self.h - 550])
        top_label = Message.Message(game_window,"AI 0", text_font, black, [self.w/2,0 + 25])
        left_label = Message.Message(game_window,"AI 1", text_font, black, [self.w*1/16, self.h*1/2])
        right_label = Message.Message(game_window,"AI 2", text_font, black, [self.w*15/16 + 25, self.h*1/2])
        main_player_label = Message.Message(game_window,"Main", text_font, black, [self.w/2, self.h*15/16 + 25])
        you_win_label = Message.Message(game_window, "YOU WIN", large_text, black, [1000, self.h - 550])
        you_lose_label = Message.Message(game_window, "YOU LOSE", large_text, black, [1000, self.h - 550])
        # card_positions.append((self.w/2, self.h*7/8))
        #     card_positions.append((self.w/8, self.h/2))
        #     card_positions.append((self.w/2, self.h*1/8))
        #     card_positions.append((self.w*7/8, self.h/2))

        #Initialize Buttons
        button_font = pygame.font.Font('Resources/Font/OpenSans-Regular.ttf', fontSize)
        draw_btn = Button.Button(game_window, red, [self.w*7/8, self.h*7/8], [fontSize*4, fontSize*2], button_font, "Draw", red, yellow)
        skip_btn = Button.Button(game_window, red, [self.w*7/8, self.h*7/8], [fontSize*4, fontSize*2], button_font, "Skip", red, yellow)

        selected_card = None
        ai_turn = True
        last_time = time()
        can_draw = True
        mouse_down = False

        total_players = self.game_instance.total_players
        card_positions = []
        if total_players==2:
            card_positions.append((self.w/2, self.h*7/8))
            card_positions.append((self.w/2, self.h*1/8))

        if total_players==3:
            card_positions.append((self.w/2, self.h*7/8))
            card_positions.append((self.w/8, self.h/2))
            card_positions.append((self.w*7/8, self.h/2))

        if total_players==4:
            card_positions.append((self.w/2, self.h*7/8))
            card_positions.append((self.w/8, self.h/2))
            card_positions.append((self.w/2, self.h*1/8))
            card_positions.append((self.w*7/8, self.h/2))

        index = self.game_instance.players.index(self.game_instance.main_player)
        player_dict = {}
        for i in range(total_players):
            print(i)
            player_dict[i] = self.game_instance.players[(index+i)%(total_players)]
            # print(player_dict[i].name)
            # if player_dict[i].name == "AI 0":
            #     top_label.changeMessage("AI 0")
            # if player_dict[i].name == "AI 1":
            #     left_label.changeMessage("AI 1")
            # if player_dict[i].name == "AI 2":
            #     right_label.changeMessage("AI 2")
            # if player_dict[i].name == "AI 0":
            #     main_player_label.changeMessage()

        while True: #not self.game_instance.winnerExists():
            if ai_turn:
                if time()-last_time > 2:
                    last_time = time()
                    if self.game_instance.nextTurn():
                        ai_turn = False
                else:
                    sleep(0.1)
            # Tries to handle the case where a winner exists
            if self.game_instance.winnerExists():
                self.showWinScreen(self.game_instance.getWinner(), game_window, you_win_label)
                break
            
            num_turns.changeMessage(str(self.game_instance.actual_turn))
            current_player_label.changeMessage(self.game_instance.getCurrPlayer())

            current_player = self.game_instance.getCurrPlayer()
            top_label.changeColor(yellow if current_player == "AI 0" else black)
            left_label.changeColor(yellow if current_player == "AI 1" else black)
            right_label.changeColor(yellow if current_player == "AI 2" else black)
            main_player_label.changeColor(yellow if current_player != "AI 0" and current_player != "AI 1" and current_player != "AI 2" else black)
            # pygame.time.delay(3000) # Pauses the game for 3 seconds
            # current_player_label.displayMessage()
            # current_player.displayMessage()

            self.card_imgs = []
            for i in range(total_players):
                updateCards(self, player_dict[i], card_positions[i], game_window)
            
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if draw_btn.isHovered() and ai_turn == False and can_draw:
                        self.game_instance.draw(self.game_instance.main_player, 1)
                        can_draw = False
                        mouse_down = True
                        print("Main player drew")
                    elif skip_btn.isHovered() and ai_turn == False and not can_draw and not mouse_down:
                        self.game_instance.skipTurn()
                        ai_turn = True
                        can_draw = True
                        print("Main player skipped turn")

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif not selected_card and event.type == pygame.MOUSEBUTTONDOWN:
                    #if draw_button.isHovered:

                    for card in self.card_imgs:
                        if card.card in self.game_instance.main_player.hand and card.isHovered():
                            selected_card = card
                            selected_card.clicked = True

                elif event.type == pygame.MOUSEBUTTONUP:
                    mouse_down = False
                    if selected_card:
                        if selected_card.checkInBounds(self.middle_bound):
                            #print(type(selected_card.card))
                            if self.game_instance.ruleset.isValid(card=selected_card.card, topCard=self.game_instance.top_card):
                                # play_card = mix.Sound('Resources/Sounds/Card-flip-sound-effect.wav')
                                # play_card.set_volume(0.5)
                                # play_card.play()
                                selected_card.updateBasePos((self.middle_bound.centerx, self.middle_bound.centery))
                                self.top_card.updateCard(self.game_instance.top_card)
                                self.game_instance.updateTurnHuman(self.game_instance.main_player, selected_card.card)
                                ai_turn = True
                                can_draw = True
                        selected_card.clicked = False
                        selected_card = None

            self.top_card.updateCard(self.game_instance.top_card)

            game_window.fill(self.bg_color)
            pos = pygame.mouse.get_pos()
            
            pygame.draw.rect(game_window, pygame.Color("White"), self.middle_bound, 2, 10)

            for card in self.card_imgs:
                card.displayImage()

            self.top_card.displayImage()

            if selected_card:
                selected_card.updatePos(pos)
                selected_card.displayImage()

            if can_draw:
                draw_btn.displayButton()
            else:
                skip_btn.displayButton()

            for label in labels:
                label.displayMessage()

            # if current_player.changeMessage:
            #     pygame.time.delay(300) # Pauses the game
            #     current_player_label.displayMessage()
            #     current_player.displayMessage()

            pygame.display.flip()
            clock.tick(60)

