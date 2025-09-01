import sys

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_WHITE, WIN_HEIGHT, EVENT_ENEMY, COLOR_YELLOW, EVENT_TIMEOUT
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window, name, menu_option):
        self.timeout = 20000
        self.window = window
        self.name = name
        self.menu_option = menu_option
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(f'{self.name}bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        # player = (EntityFactory.get_entity('Player1'))
        # player.score = score
        # self.entity_list.append(player)
        # self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY, 500)
        pygame.time.set_timer(EVENT_TIMEOUT, 100)

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, Player):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.nome == 'Player1':
                    self.level_text(14, f'Player - Health: {ent.health}  |  Score: {ent.score}', COLOR_YELLOW, (10, 25))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity('Enemy'))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= 100
                    if self.timeout == 0:
                        # for ent in self.entity_list:
                        #     if isinstance(ent, Player):
                        #         score[0] = ent.score
                        return True
                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True
                if not found_player:
                    return False

            # printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(14, 'RU: 4678731', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, 'ELIEL RODRIGUES', COLOR_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
