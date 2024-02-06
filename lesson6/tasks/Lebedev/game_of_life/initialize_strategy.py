from abc import ABC, abstractmethod
import random
from cell import Cell


class InitializeStrategy(ABC):
    @abstractmethod
    def initialize_cells(self, width, height) -> list[list[Cell]]:
        pass


class InitializeRandomStrategy(InitializeStrategy):
    def initialize_cells(self, width, height):
        cells = [[Cell(random.choice([True, False])) for j in range(width)] for i in range(height)]

        return cells
