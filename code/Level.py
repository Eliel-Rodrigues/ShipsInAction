import pygame.display

from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, nome, menu_option):
        self.window = window
        self.nome = nome
        self.menu_option = menu_option
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1bg'))

    def run(self):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()
        pass
