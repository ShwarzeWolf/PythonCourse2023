from math import pi


shape_type = input("Enter the shape type: ")
if shape_type == "square":
    square_side = int(input("Enter the side of the square: "))
    print(square_side ** 2)
elif shape_type == "circle":
    radius = int(input("Enter the radius of the circle: "))
    print(pi * (radius ** 2))
elif shape_type == "rectangle":
    rectangle_side_a, rectangle_side_b = map(int, input("Enter the 2 sides of the rectangle separated by a space: ").split())
    print(rectangle_side_a * rectangle_side_b)
else:
    print("Unknown shape")
