f = int(input("Введите число фигур, площадь которых вам нужно узнать:"))
m=0
n=0
for i in range(f):
    a = input()
    a1 = a.lower()
    if a1 == "square":
        b = float(input())
        m=b*b
        print(m)
    elif a1 == "circle":
        c = float(input())
        m= 3.14 * c * c
        print(m)
    elif a1 == "rectangle":
        b = float(input())
        c = float(input())
        m=b*c
        print(m)
    else:
        print("Unknown shape")
    n+=m
print(f"Общее количество фигур: {f}")
print(f"Суммарная площадь всех фигур: {n}")


