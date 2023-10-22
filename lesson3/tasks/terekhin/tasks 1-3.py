n = int(input("Посчитать площадь у фигур в кол-ве: "))
amount_figure = n
sum_s = 0
for i in range(n):
    figure_type = input('Фигура: ').lower()
    if figure_type == 'square':
        a = float(input('Длинна стороны: '))
        s = a ** 2
        sum_s += s
        print(f'Площадь квадрата со стороной {a} равна {s}')
    elif figure_type == 'circle':
        r = float(input('Радиус круга: '))
        s = 3.14 * (r ** 2)
        sum_s += s
        print(f'Площадь круга радиуса {r} равна {s}')
    elif figure_type == 'rectangle':
        a, b = int(input('Длинна прямоугольника: ')), int(input('Ширина прямоугольника: '))
        s = a * b
        sum_s += s
        print(f'Площадь прямоугольника со сторонами {a} и {b} равна {s}')
    else:
        amount_figure -= 1
        print('Unknown shape')
print(f'Суммарная площадь {amount_figure} введённых фигур равна {sum_s}')