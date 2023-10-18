# Задание 1-3
import math
howmany = int(input('введите количество фигур: '))
if howmany <= 0:
    print('error')
else:

    summ=0
    for i in range (howmany):
        figures = input('введите название фигуры (circle or rectangle or square) : ').lower()
        if figures == "square":
            a = int(input('введите сторону a: '))
            S=a**2
            summ += S
        elif figures == 'circle':
            r = int(input('введите радиус окружности r: '))
            S = (math.pi) * (r ** 2)
            summ += S
        elif figures == 'rectangle':
            a = int(input('введите сторону a: '))
            b = int(input('введите сторону b: '))
            S=a*b
            summ += S
        else:
            print('Фигура не распознана')

    print('было посчитано: ', howmany,
        "Сумма площадей: ",summ)



#  Задание 5
# a=str(input())
# if a[0]==')':
#     print('False')
# else:
#     while '()' in a:
#         a=a.replace("()",'')
#     if a == '':
#         print('True')
#     else:
#         print('False')
