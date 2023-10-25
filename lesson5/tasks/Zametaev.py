import random
import time

#Игра жизнь

"""
Живые клетки 💖
Мёртвые клетки ⚫

Если хотите начать введите 2 числа через пробел
"""
def draw_field(field):
    for row in field:
        print(' '.join(['💖' if cell else '⚫' for cell in row]))
    print()

def live(i, j):
    count = 0
    for x in range(max(0, i - 1), min(n, i + 2)):
        for y in range(max(0, j - 1), min(m, j + 2)):
            if not (x == i and y == j):
                count += field[x][y]
    return count

def next_new():
    new_field = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            live_neighbors = live(i, j)
            if field[i][j]:
                if live_neighbors in [2, 3]:
                    new_field[i][j] = 1
            else:
                if live_neighbors == 3:
                    new_field[i][j] = 1
    return new_field


n, m = map(int, input().split())


field = [[random.choice([0, 1]) for _ in range(m)] for _ in range(n)]

"""
Живые клетки 💖
Мёртвые клетки ⚫

Если хотите начать введите 2 числа через пробел
"""


while True:
    draw_field(field)
    new_field = next_new()
    if new_field == field:
        break
    field = new_field
    time.sleep(1)
    print("Следующее поле")
