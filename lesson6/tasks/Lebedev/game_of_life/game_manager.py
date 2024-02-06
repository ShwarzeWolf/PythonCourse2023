import time
from field import Field
from initialize_strategy import InitializeRandomStrategy, InitializeStrategy
from cell import Cell


class GameManager:
    __board_positions = []

    def start(self, width, height, strategy: InitializeStrategy):
        field = Field()
        field.initialize_cells(width, height, strategy)
        
        
        while True:
            position = field.get_flat_field_position()
            str_representation = "".join([cell.__repr__() for cell in position])

            field.draw()

            if not self.check_game_conditions(position, str_representation):
                break

            self.__board_positions.append(str_representation)

            field.update()
            print()
            time.sleep(1)


    def check_game_conditions(self, new_position: list[Cell], string_representation: str):
        if string_representation in self.__board_positions:
            print("Position repeated")
            print("Game is over")
            # If the new position is already in the positions stack, then the game should end
            return False
        
        if not any([cell.get_is_alive() for cell in new_position]):
            print("No cells alive")
            print("Game is over")
            # If the new position contains only dead cells, then the game should end
            return False

        return True
