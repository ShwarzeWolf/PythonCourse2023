from math import pi


number = int(input("Enter number of shapes: "))
n = 0
sum_of_areas = 0
for i in range(number):
    shape_type = input("Enter the shape type: ")
    shape_type = shape_type.lower()
    if shape_type == "square":
        square_side = int(input("Enter the side of the square: "))
        n += 1
        sum_of_areas = square_side ** 2
    elif shape_type == "circle":
        radius = int(input("Enter the radius of the circle: "))
        n += 1
        sum_of_areas += pi * (radius ** 2)
    elif shape_type == "rectangle":
        rectangle_side_a, rectangle_side_b = \
            map(int, input("Enter the 2 sides of the rectangle separated by a space: ").split())
        n += 1
        sum_of_areas += rectangle_side_a * rectangle_side_b
    else:
        print("Unknown shape")
print(f"Total figures: {n}\nSum of areas: {sum_of_areas}")
