""" 1 """
import math

def calc_area(shape):
    if shape == "квадрат":
        side = float(input("Введите длину каждой стороны: "))
        area = side**2
        print("Площадь квадрата:", area)
    elif shape == "круг":
        radius = float(input("Введите радиус: "))
        area = math.pi * (radius ** 2)
        print("Площадь круга:", area)
    elif shape == "прямоугольник":
        side1 = float(input("Введите длину первой стороны: "))
        side2 = float(input("Введите длину второй стороны: "))
        area = side1 * side2
        print("Площадь прямоугольника:", area)
    else:
        print("Неизвестная фигура")

shape = input("Введите фигуру: ")
calc_area(shape)

""" 2 """

import math

def calc_area(shape):
    if shape == "квадрат":
        side = float(input("Введите длину каждой стороны: "))
        area = side**2
        print("Площадь квадрата:", area)
    elif shape == "круг":
        radius = float(input("Введите радиус: "))
        area = math.pi * (radius ** 2)
        print("Площадь круга:", area)
    elif shape == "прямоугольник":
        side1 = float(input("Введите длину первой стороны: "))
        side2 = float(input("Введите длину второй стороны: "))
        area = side1 * side2
        print("Площадь прямоугольника:", area)
    else:
        print("Неизвестная фигура")

shape = input("Введите фигуру: ").lower()
calc_area(shape)

""" 3 """

import math

def calc_area(shape):
    if shape == "квадрат":
        side = float(input("Введите длину каждой стороны: "))
        area = side**2
        print("Площадь квадрата:", area)
        return area
    elif shape == "круг":
        radius = float(input("Введите радиус: "))
        area = math.pi * (radius ** 2)
        print("Площадь круга:", area)
        return area
    elif shape == "прямоугольник":
        side1 = float(input("Введите длину первой стороны: "))
        side2 = float(input("Введите длину второй стороны: "))
        area = side1 * side2
        print("Площадь прямоугольника:", area)
        return area
    else:
        print("Неизвестная фигура")
        return 0

num_figures = int(input("Введите количество фигур: "))
total_area = 0

for i in range(num_figures):
    shape = input("Введите фигуру: ").lower()
    figure_area = calc_area(shape)
    total_area += figure_area

print(f"Рассчитано {num_figures} фигур, суммарная площадь: {total_area}")
