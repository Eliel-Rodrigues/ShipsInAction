from code.Background import Background
from code.Const import WIN_HEIGHT, WIN_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_nome: str, position=(0, 0)):
        match entity_nome:
            case 'Level1bg':
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(f'Level1bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1bg{i}', (0, -WIN_HEIGHT)))

                print(list_bg)
                return list_bg
