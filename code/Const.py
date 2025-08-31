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
    'Player1at': 2,
    'Player2': 3,
    'Enemy': 4
}

ENTITY_HEALTH = {
    'Level1bg0': 999,
    'Level1bg1': 999,
    'Level1bg2': 999,
    'Player1': 200,
    'Player1at': 1,
    'Player2': 200,
    'Enemy': 20

}
# M
MENU_OPTION = ('NEW GAME',
               'SCORE',
               'EXIT')
#W
WIN_WIDTH = 576
WIN_HEIGHT = 324