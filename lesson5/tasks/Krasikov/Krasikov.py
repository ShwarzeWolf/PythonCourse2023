import random
import time
import copy
import os.path

alive = "#"    # Символ для отображения живых клеток
dead = "_"     # Символ для отображения метрвых клеток
simulation_speed = 10   # Скорость симуляции

# Заданный массив
n = 10
m = 10
board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# Случайное заполнение
# n = int(input("Enter width: "))
# m = int(input("Enter height: "))
# board = [[random.randint(0, 1) for _ in range(n)] for _ in range(m)]

# Чтение из файла board.txt
# f = open(os.path.abspath("Krasikov/board.txt"), 'r')
# data = f.readlines()
# n = len(data[0])-1
# m = len(data)
# board = []
# for i in range(n):
#     line = []
#     for j in range(m):
#         line.append(int(data[i][j]))
#     board.append(line)


next_board = copy.deepcopy(board)
prev_board = copy.deepcopy(board)


def find_neighbours(_x, _y):    # Функция для подсчета количества соседних клеток
    count = 0
    for i in [_x - 1, _x, 0 if _x + 1 == m else _x + 1]:
        for j in [_y - 1, _y, 0 if _y + 1 == n else _y + 1]:
            if board[i][j] == 1 and (i != _x or j != _y):
                count += 1
    return count


while 1:
    print("\n"*5)  # Отрисовка текущего массива в консоль
    print("  ", end="")
    for i in range(n):
        print(i, end=" ")
    print()
    for y_ in range(m):
        print(y_, end=" ")
        for x_ in range(n):
            print(alive if board[y_][x_] == 1 else dead, end=" ")
            # print(board[y_][x_], end="")
        print()

    for x in range(n):  # Изменение next_board по правилам игры, используя find_neighbours() для поиска соседей
        for y in range(m):
            counter = find_neighbours(x, y)

            if counter == 3 and board[x][y] == 0:
                next_board[x][y] = 1
                # print(f"New cell at {x}:{y}")
                continue
            if (counter < 2 or counter > 3) and board[x][y] == 1:
                next_board[x][y] = 0
                # print(f"Cell died at {x}:{y}")
                continue

    time.sleep(10 / simulation_speed)   # Задержка
    if prev_board == [[0]*n]*m:
        print("No living cells")
        break
    if board == next_board:
        print("No changes")
        break
    if prev_board == next_board:
        print("Repeating")
        break
    prev_board = copy.deepcopy(board)
    board = copy.deepcopy(next_board)