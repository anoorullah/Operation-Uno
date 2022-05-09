import pygame
from Screens import MainMenu, GameWindow
from Game import Game

if __name__ == '__main__':
    pygame.init()
    info = pygame.display.Info()
    screen_w, screen_h = info.current_w, info.current_h

    # Main theme song
    # menu_sound = pygame.mixer.Sound('Resources/Sounds/Menu-theme.wav')
    # menu_sound.set_volume(0.4)
    # pygame.mixer.Channel(0).play(menu_sound)
    pygame.mixer.music.load('Resources/Sounds/Menu-theme.wav')
    pygame.mixer.music.play(-1)

    main_menu = MainMenu.MainMenu(w=info.current_w, h=info.current_h-25)
    main_menu.display()

    # for quick testing of game_window
    # game_instance = Game(screen_w, screen_h-50, False, 3, 'Easy')
    # game_window = GameWindow_test.GameWindow_test(game_instance, screen_w, screen_h-50)
    # game_window.display()


