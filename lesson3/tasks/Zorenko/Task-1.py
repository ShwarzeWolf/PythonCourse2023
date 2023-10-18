a = input()
if a == "square":
    b = float(input())
    print(b * b)
if a == "circle":
    c = float(input())
    print(3.14*c*c)
if a == "rectangle":
    b=float(input())
    c=float(input())
    print(b*c)
else:
    print("Unknown shape")
