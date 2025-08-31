from abc import ABC, abstractmethod

import pygame.image

from code.Const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE


class Entity(ABC):
    def __init__(self, nome: str, position: tuple):
        self.nome = nome
        self.surf = pygame.image.load(f'./assets/{nome}.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.nome]
        self.damage = ENTITY_DAMAGE[self.nome]
        self.score = ENTITY_SCORE[self.nome]
        self.lest_dmg = 'None'

    @abstractmethod
    def move(self):
        pass
