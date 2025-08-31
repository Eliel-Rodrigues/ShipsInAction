# C
import pygame

COLOR_BLACK = (0,0,0)
COLOR_WHITE = (255,255,255)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Level1bg0': 0,
    'Level1bg1': 1,
    'Level1bg2': 2,
    'Player1': 3,
    'Player2': 3,
    'Enemy': 4

}
# M
MENU_OPTION = ('NEW GAME SHIP 1',
               'NEW GAME SHIP 2',
               'SCORE',
               'EXIT')
#W
WIN_WIDTH = 576
WIN_HEIGHT = 324