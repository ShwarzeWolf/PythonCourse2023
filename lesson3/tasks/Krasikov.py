# Задание 1-3
total_square = 0
to_count = int(input("Введите количество фигур: "))
for i in range(to_count):
    shape = input("Введите тип фигуры: ").lower()
    if shape == "square":
        result = int(input("Введите сторону квадрата: "))**2
        print(result)
        total_square += result
    elif shape == "circle":
        result = (int(input("Введите радиус круга: "))**2)*3.14
        print(result)
        total_square += result
    elif shape == "rectangle":
        result = int(input("Введите первую сторону прямоугольника: "))*int(input("Введите вторую сторону прямоугольника: "))
        print(result)
        total_square += result
    else:
        print("Unknown shape")
print(f'Фигур посчитано: {to_count}, суммарная площадь: {total_square}')


# Задание 4
a = input().lower()
for index in range(len(a) // 2):
    if a[index] != a[-index-1]:
        print("Не палиндром")
        break
else:
    print("Палиндром")


# Задание 5
string = input()
counter = 0
for i in string:
    if i == '(':
        counter += 1
    if i == ')':
        counter -= 1
        if counter < 0:
            break
if counter == 0:
    print("Правильная последовательность")
else:
    print("Неправильная последовательность")


# Задание 6
a = input()
b = input()
counter = 0
for i in b:
    if i == a[counter]:
        counter += 1
        if counter == len(a):
            print("True")
            break
    else:
        counter = 0
        if i == a[counter]:
            counter += 1
            if counter == len(a):
                print("True")
                break
else:
    print("False")
