import pygame.key

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH
from code.Entity import Entity
from code.PlayerAt import PlayerAt


class Player(Entity):
    def __init__(self, nome: str, position: tuple):
        super().__init__(nome, position)
        self.shot_delay = 20

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP] and self.rect.top >= 0:
            self.rect.centery -= ENTITY_SPEED[self.nome]
        if pressed_key[pygame.K_DOWN] and self.rect.bottom <= WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.nome]
        if pressed_key[pygame.K_LEFT] and self.rect.left >= 0:
            self.rect.centerx -= ENTITY_SPEED[self.nome]
        if pressed_key[pygame.K_RIGHT] and self.rect.right <= WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.nome]

    def shoot(self):
        self.shot_delay -= 20
        if self.shot_delay == 0:
            self.shot_delay = 20
            pressed_key = pygame.key.get_pressed()
            if pressed_key[pygame.K_LCTRL]:
                return PlayerAt(nome=f'Player1at', position=(self.rect.centerx, self.rect.centery))

