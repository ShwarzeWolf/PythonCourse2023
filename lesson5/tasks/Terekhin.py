from copy import deepcopy
from random import randint
import time

COORD = False  # отображение координат
PAUSE_TIME_IN_SECONDS = 0.5  # задержка между итерациями в секундах
HEIGHT = 5  # высота поля
WIDTH = 5  # ширина поля

field = [[randint(0, 1) for x in range(WIDTH)] for y in range(HEIGHT)]  # создание и заполнение поля


def coord_normalization(cord):
    for dot in range(len(cord)):
        if cord[dot][0] < 0:
            cord[dot][0] = HEIGHT - 1
        if cord[dot][0] > HEIGHT - 1:
            cord[dot][0] = 0
        if cord[dot][1] < 0:
            cord[dot][1] = WIDTH - 1
        if cord[dot][1] > WIDTH - 1:
            cord[dot][1] = 0
    return cord


def check_neighbors(field, y_cor, x_cor):
    living_neighbor = 0
    cord = []  # список координат соседних точек

    for y1 in range(-1, 2):
        for x1 in range(-1, 2):
            cord.append([y_cor + y1, x_cor + x1])
    cord.remove([y_cor, x_cor])  # удаление координаты самой точки

    cord = coord_normalization(cord)

    for item in range(len(cord)):
        if field[cord[item][0]][cord[item][1]] == 1:
            living_neighbor += 1
    return living_neighbor


def step(field):
    new_field = deepcopy(field)
    for y_cor in range(HEIGHT):
        for x_cor in range(WIDTH):
            living_neighbor = check_neighbors(field, y_cor, x_cor)
            if field[y_cor][x_cor] == 1 and living_neighbor < 2:
                new_field[y_cor][x_cor] = 0
            if field[y_cor][x_cor] == 1 and living_neighbor > 3:
                new_field[y_cor][x_cor] = 0
            if field[y_cor][x_cor] == 0 and living_neighbor == 3:
                new_field[y_cor][x_cor] = 1
    return new_field


old_field = []  # копия предыдущего состояния поля

while field != old_field:

    old_field = deepcopy(field)

    #  вывод поля в консоль
    if COORD:
        for i in range(WIDTH + 1):
            print(i, end=' ')
        for i in range(HEIGHT):
            print(f"\n{i + 1} {str(field[i]).replace(',', '')[1:-1]}", end='')
    else:
        for i in range(HEIGHT):
            print(str(field[i]).replace(',', '')[1:-1])
    print('\n')

    field = step(field)

    time.sleep(PAUSE_TIME_IN_SECONDS)  # задержка между итерациями
