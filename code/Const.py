# C
import pygame

COLOR_BLACK = (0,0,0)
COLOR_WHITE = (255,255,255)
COLOR_YELLOW = (225,225,128)

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
    'Enemy': 20
}

ENTITY_DAMAGE = {
    'Level1bg0': 0,
    'Level1bg1': 0,
    'Level1bg2': 0,
    'Player1': 1,
    'Player1at': 10,
    'Enemy': 100
}

ENTITY_SCORE = {
    'Level1bg0': 0,
    'Level1bg1': 0,
    'Level1bg2': 0,
    'Player1': 0,
    'Player1at': 0,
    'Enemy': 100
}
# M
MENU_OPTION = ('NEW GAME',
               'SCORE',
               'EXIT')
#W
WIN_WIDTH = 576
WIN_HEIGHT = 324