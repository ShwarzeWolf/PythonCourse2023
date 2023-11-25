# Есть три способа заполнения:
# Заданный массив, случайное
# заполнение и из файла board.txt
# При паузе (буква P) можно
# менять состояние клеток кликом мыши

import random
import time
import copy
import os.path
from tkinter import *

simulation_speed = 10   # Скорость симуляции
paused = False
mouse_x = mouse_y = 0
tk = Tk()
tk.title("Game of Life")
tk.resizable(0, 0)


# Заданный массив:

n = 11
m = 11
board = [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
         [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# Случайное заполнение:

# n = int(input("Enter width: "))
# m = int(input("Enter height: "))
# board = [[random.randint(0, 1) for _ in range(n)] for _ in range(m)]

# Чтение из файла board.txt:

# print(os.path.abspath(""))
# f = open(os.path.abspath("Krasikov/board.txt"), 'r')
# data = f.readlines()
# f.close()
# n = len(data[0])-1
# m = len(data)
# board = []
# for i in range(n):
#     line = []
#     for j in range(m):
#         line.append(int(data[i][j]))
#     board.append(line)


def pause(event):
    global paused
    if event.char == "p":
        paused = not paused


canvas = Canvas(tk, width=50*n, height=50*m)    # Создание и размещение клеток на холсте
canvas.pack()
cell = [[canvas.create_rectangle(0, 0, 50, 50, fill="white") for _ in range(n)] for _ in range(m)]
for x in range(n):
    for y in range(m):
        canvas.coords(cell[x][y], x*50, y*50, 50+x*50, 50+y*50)
tk.bind("<KeyPress>", pause)

next_board = copy.deepcopy(board)
prev_board = copy.deepcopy(board)


def mouse_pos(event):   # Функция для получения позиции мыши
    global mouse_x, mouse_y
    mouse_x = event.x
    mouse_y = event.y


def mouse_click(event):    # Функция для обработки кликов мыши на клетки
    global paused, next_board, prev_board
    if paused and mouse_y < m*50 and mouse_x < n*50:
        if board[mouse_x // 50][mouse_y // 50] == 0:
            board[mouse_x // 50][mouse_y // 50] = 1
        else:
            board[mouse_x // 50][mouse_y // 50] = 0
        next_board = copy.deepcopy(board)
        prev_board = copy.deepcopy(board)


tk.bind("<Motion>", mouse_pos)
tk.bind("<ButtonPress>", mouse_click)


def find_neighbours(_x, _y):    # Функция для подсчета количества живых соседних клеток
    count = 0
    for i in [_x - 1, _x, 0 if _x + 1 == m else _x + 1]:
        for j in [_y - 1, _y, 0 if _y + 1 == n else _y + 1]:
            if board[i][j] == 1 and (i != _x or j != _y):
                count += 1
    return count


def update_canvas():    # Функция для обновления холста
    for x in range(n):
        for y in range(m):
            canvas.itemconfigure(cell[x][y], fill="black" if board[x][y] == 1 else "white")
    canvas.update()


while 1:
    update_canvas()
    if paused:
        continue
    for x in range(n):  # Изменение next_board по правилам игры, используя find_neighbours() для поиска соседей
        for y in range(m):
            counter = find_neighbours(x, y)

            if counter == 3 and board[x][y] == 0:
                next_board[x][y] = 1
                continue
            if (counter < 2 or counter > 3) and board[x][y] == 1:
                next_board[x][y] = 0
                continue
    time.sleep(10 / simulation_speed)   # Задержка
    if board == [[0]*n]*m:
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