from abc import ABC, abstractmethod
import math
from typing import Optional


class AbstractShape(ABC):
    ''' Class representing any shape '''
    def calculate_area(self):
        ''' Inputs values and returns the area of the shape '''
        self.get_values()
        return self.area_formula()

    @abstractmethod
    def get_values(self):
        ''' Method to input values '''
        pass

    @abstractmethod
    def area_formula(self) -> float:
        ''' Method to calculate area from values in the class '''
        pass


class SquareShape(AbstractShape):
    def get_values(self):
        self.length = float(input("Введите длину стороны квадрата: "))
    
    def area_formula(self):
        return self.length ** 2


class CircleShape(AbstractShape):
    def get_values(self):
        self.radius = float(input("Введите радиус круга: "))
    
    def area_formula(self):
        area = math.pi * (self.radius ** 2)
        return round(area, 2)
    

class RectangleShape(AbstractShape):
    def get_values(self):
        self.width = float(input("Введите 1-ю сторону прямоугольника: "))
        self.height = float(input("Введите 2-ю сторону прямоугольника: "))
    
    def area_formula(self):
        return self.width * self.height


def determine_shape(shape_name: str) -> Optional[AbstractShape]:
    '''
    Returns a shape object by its type name

    :param shape_name: name of the shape ("square", "circle", "rectangle")
    :returns: shape object or None if shape is not found
    '''
    shape_name = shape_name.lower()
    if shape_name == "square":
        return SquareShape()
    elif shape_name == "circle":
        return CircleShape()
    elif shape_name == "rectangle":
        return RectangleShape()
    else:
        print("Unknown shape")
        return None


if __name__ == "__main__":
    shapes_count = int(input("Введите количество фигур, площадь которых вы хотите рассчитать: "))

    total_area = 0
    successful_count = 0

    for i in range(shapes_count):
        print()

        shape_name = input("Введите тип фигуры: ")
        shape = determine_shape(shape_name)

        if shape == None:
            continue

        area = shape.calculate_area()
        print(f"Площадь фигуры равна {area}")

        total_area += area
        successful_count += 1

    print("________________________________________________________________")
    print(f"Общая площадь: {total_area}")
    print(f"Было посчитано {successful_count} площадей фигур")
