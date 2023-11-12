from copy import deepcopy
from random import randint
import pygame

SCREEN_HEIGHT = 900  # высота окна
SCREEN_WIDTH = 1600  # ширина окна
TILE_SIZE = 25  # размер клетки в пикселях
FPS = 10  # кол-во кадров в секунду
TIlE_WIDTH, TILE_HEIGHT = SCREEN_WIDTH // TILE_SIZE, SCREEN_HEIGHT // TILE_SIZE

# инициализация окна игры
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()

# создание и заполнение поля
field = [
    [randint(0, 1) for x in range(TIlE_WIDTH)]
    for y in range(TILE_HEIGHT)
]


def check_neighbors(field, y_cor, x_cor):
    living_neighbor = 0

    for y1 in range(y_cor - 1, y_cor + 2):
        for x1 in range(x_cor - 1, x_cor + 2):
            if field[y1 % TILE_HEIGHT][x1 % TIlE_WIDTH] == 1:
                living_neighbor += 1

    if field[y_cor][x_cor] == 1:
        living_neighbor -= 1

    return living_neighbor


def step(field):
    new_field = deepcopy(field)  # создание следующего варианта поля

    for y_cor in range(TILE_HEIGHT):
        for x_cor in range(TIlE_WIDTH):
            living_neighbor = check_neighbors(field, y_cor, x_cor)
            if field[y_cor][x_cor] == 1 and living_neighbor < 2:
                new_field[y_cor][x_cor] = 0
            if field[y_cor][x_cor] == 1 and living_neighbor > 3:
                new_field[y_cor][x_cor] = 0
            if field[y_cor][x_cor] != 1 and living_neighbor == 3:
                new_field[y_cor][x_cor] = 1

    return new_field


while True:

    # отрисовка окна игры
    screen.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # отрисовка сетки (поля)
    [pygame.draw.line(
        screen,
        pygame.Color('darkslategrey'),
        (x, 0),
        (x, SCREEN_HEIGHT))
        for x in range(0, SCREEN_WIDTH, TILE_SIZE)]
    [pygame.draw.line(
        screen,
        pygame.Color('darkslategrey'),
        (0, y),
        (SCREEN_WIDTH, y))
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE)]

    # отрисовка живых клеток
    for x in range(TIlE_WIDTH):
        for y in range(TILE_HEIGHT):
            if field[y][x]:
                pygame.draw.rect(
                    screen,
                    pygame.Color('green'),
                    (
                        x * TILE_SIZE + 2,
                        y * TILE_SIZE + 2,
                        TILE_SIZE - 2,
                        TILE_SIZE - 2
                    )
                )

    field = step(field)  # переход к следующей итерации

    pygame.display.flip()  # вывод кадра игры
    clock.tick(FPS)  # задержка между кадрами
