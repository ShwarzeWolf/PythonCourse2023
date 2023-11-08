import copy
import time
import initialize_strategy
from cell import Cell


class Field:
    def __init__(self) -> None:
        self.cells = []
    
    def initialize_cells(self, width, height, strategy: initialize_strategy.InitializeStrategy):
        self.cells = strategy.initialize_cells(width, height)
        self.width = width
        self.height = height
    
    def get_neighbors(self, row_idx, column_idx) -> list[Cell]:
        neighbors = []
        for x_offset in range(-1, 2):
            for y_offset in range(-1, 2):
                if (x_offset, y_offset) == (0, 0):
                    continue

                row = row_idx + y_offset
                col = column_idx + x_offset

                if row >= self.height:
                    row = 0

                if col >= self.width:
                    col = 0

                if row <= -1:
                    row = self.height - 1

                if col <= -1:
                    col = self.width - 1
                
                neighbor_cell = self.cells[row][col]
                neighbors.append(neighbor_cell)

        return neighbors

    def update(self):
        new_cells = copy.deepcopy(self.cells)

        for row_idx, row in enumerate(self.cells):
            for column_idx, cell in enumerate(row):
                neighbors = self.get_neighbors(row_idx, column_idx)
                alive_neighbors_amount = sum([neighbor.get_is_alive() for neighbor in neighbors])

                new_cell = new_cells[row_idx][column_idx]
                if cell.get_is_alive():
                    if alive_neighbors_amount <= 1:
                        new_cell.set_is_alive(False)
                    elif 2 <= alive_neighbors_amount <= 3:
                        new_cell.set_is_alive(True)
                    elif alive_neighbors_amount > 3:
                        new_cell.set_is_alive(False)
                else:
                    if alive_neighbors_amount == 3:
                        new_cell.set_is_alive(True)

        self.cells = new_cells
        
    def draw(self):
        for row in self.cells:
            print(" ".join([cell.__repr__() for cell in row]))
    
    def get_flat_field_position(self) -> list[Cell]:
        flat_position = []
        for row in self.cells:
            flat_position += row
        return flat_position
