from abc import abstractmethod
import math


class AbstractShape:
    def calculate_area(self):
        self.get_values(self)
        return self.area_formula(self)

    @abstractmethod
    def get_values(self):
        pass

    @abstractmethod
    def area_formula(self) -> float:
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
        square = math.pi * (self.radius ** 2)
        return round(square, 2)
    

class RectangleShape(AbstractShape):
    def get_values(self):
        self.width = float(input("Введите 1-ю сторону прямоугольника: "))
        self.height = float(input("Введите 2-ю сторону прямоугольника: "))
    
    def area_formula(self):
        return self.width * self.height


def determine_shape(shape_name):
    shape_name = shape_name.lower()
    if shape_name == "square":
        return SquareShape
    elif shape_name == "circle":
        return CircleShape
    elif shape_name == "rectangle":
        return RectangleShape
    else:
        print("Unknown shape")
        return None


shapes_count = int(input("Введите количество фигур, площадь которых вы хотите рассчитать: "))

total_square = 0
successful_count = 0

for i in range(shapes_count):
    print()

    shape_name = input("Введите тип фигуры: ")
    shape = determine_shape(shape_name)

    if shape == None:
        continue

    square = shape.calculate_area(shape)
    print(f"Площадь фигуры равна {square}")

    total_square += square
    successful_count += 1

print("________________________________________________________________")
print(f"Общая площадь: {total_square}")
print(f"Было посчитано {successful_count} площадей фигур")
