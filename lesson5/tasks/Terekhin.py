from copy import deepcopy
from random import randint
import time

COORD = False  # отображение координат

pause_time = 1  # задержка в итерациях
height = 10  # высота поля
width = 10  # ширина поля

# создание и заполнение поля
field = [[] for num in range(height)]
for i in range(len(field)):
    for x in range(width):
        field[i].append(randint(0, 1))


def coord_normalization(cord):
    for dot in range(len(cord)):
        if cord[dot][0] < 0:
            cord[dot][0] = height - 1
        if cord[dot][0] > height - 1:
            cord[dot][0] = 0
        if cord[dot][1] < 0:
            cord[dot][1] = width - 1
        if cord[dot][1] > width - 1:
            cord[dot][1] = 0
    return cord


def check_neighbors(field, y_cor, x_cor):
    living_neighbor = 0
    cord = []
    for y1 in range(-1, 2):
        for x1 in range(-1, 2):
            cord.append([y_cor + y1, x_cor + x1])
    cord.remove([y_cor, x_cor])
    cord = coord_normalization(cord)
    for item in range(len(cord)):
        if field[cord[item][0]][cord[item][1]] == 1:
            living_neighbor += 1
    return living_neighbor


def step(field):
    new_field = deepcopy(field)
    for y_cor in range(height):
        for x_cor in range(width):
            living_neighbor = check_neighbors(field, y_cor, x_cor)
            if field[y_cor][x_cor] == 1 and living_neighbor < 2:
                new_field[y_cor][x_cor] = 0
            if field[y_cor][x_cor] == 1 and living_neighbor > 3:
                new_field[y_cor][x_cor] = 0
            if field[y_cor][x_cor] == 0 and living_neighbor == 3:
                new_field[y_cor][x_cor] = 1
    return new_field


old_field = []
while field != old_field:
    old_field = deepcopy(field)
    if COORD:
        numbs = ''
        for i in range(width + 1):
            numbs += f'{i} '
        print(numbs)
        for i in range(height):
            print(f"{i + 1} {str(field[i]).replace(',', '')[1:-1]}")
    else:
        for i in range(height):
            print(str(field[i]).replace(',', '')[1:-1])
    print('')

    field = step(field)

    time.sleep(pause_time)
