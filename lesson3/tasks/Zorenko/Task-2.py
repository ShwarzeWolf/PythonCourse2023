a = input()
a1 = a.lower()
if a1 == "square":
    b = float(input())
    print(b * b)
if a1 == "circle":
    c = float(input())
    print(3.14 * c * c)
if a1 == "rectangle":
    b = float(input())
    c = float(input())
    print(b * c)
else:
    print("Unknown shape")
