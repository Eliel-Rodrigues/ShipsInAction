import random

from code.Background import Background
from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_nome: str, position=(0, 0)):
        match entity_nome:
            case 'Level1bg':
                list_bg = []
                for i in range(3):
                    list_bg.append(Background(f'Level1bg{i}', (0 + 20 * i, 0)))
                    list_bg.append(Background(f'Level1bg{i}', (0 + 120 * i, -WIN_HEIGHT)))
                return list_bg

            case 'Player1':
                return Player('Player1', ((WIN_WIDTH / 2), 230))
            case 'Player2':
                return Player('Player2', ((WIN_WIDTH / 2), 230))
            case 'Enemy':
                return Enemy('Enemy', (random.randint(40, WIN_WIDTH - 40), - 60))
