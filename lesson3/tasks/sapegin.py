#    Задание 1, 2, 3
import math
print("Задание 1 - 3")
n = int(input("Введите количество фигур, площадь которых вы хотите посчитать: "))
x = ""
y = ""
c = 0
summa = 0
for i in range(n):
    type = input("Введите тип фигруры: ").lower()
    if type == "square":
        x = int(input("Введите длину стороны квадрата: "))
        print("Площадь квадрата = ", x ** 2)
        c += 1
        summa += x ** 2
    elif type == "circle":
        x = int(input("Введите радиус круга: "))
        print("Площадь круга = ", math.pi * x ** 2)
        c += 1
        summa += math.pi * x ** 2
    elif type == "rectangle":
        x = int(input("Введите первую сторону прямоугльника: "))
        y = int(input("Введите вторую сторону прямогольника: "))
        print("Площадь прямоугльника = ", x * y)
        c += 1
        summa += x * y
    else:
        print("Unknown shape")
else:
    print("Было посчитано площадей фигур: ", c)
    print("Сумма всех посчитанных площадей = ", summa)



#     Задание 4
print("Задание 4")
a = input("Введите строку: ")
for i in range(len(a) // 2):
    if a[i] != a[-i-1]:
        print("Строка не является палиндромом")
        break
else:
    print("Строка является палиндромом")



#     Задание 5
print("Задание 5")
z = input()
count = 0
maxi = len(z) // 2
for i in z:
    if i == "(":
        count += 1
    elif i == ")":
        count -= 1
    else:
        print("Ошибка ввода")
        break
    if count < 0 or count > maxi:
        print("Последовательность неправильная")
        break
else:
    print("Последовательность правильная")



#     Задание 6
print("Задание 6")
str = input()
search = input()
if search in  str:
    print("Вторая строка есть в первой")
else:
    print("Второй строки нет в первой")








