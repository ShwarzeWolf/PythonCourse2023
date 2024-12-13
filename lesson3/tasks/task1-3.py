a = int(input())
for i in range(a):
    type_figure = input().lower()
    if type_figure == "square":
        a = int(input())
        print(a**2)
    elif type_figure == "circle":
        r = int(input())
        print(3.14*r*2)
    elif type_figure == "rectangle":
        a = int(input())
        b = int(input())
        print(a*b)
    else:
        print("Unknown shape")
