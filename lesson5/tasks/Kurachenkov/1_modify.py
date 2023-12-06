import random
import time

"""
Мёртвые клетки - " " (пустота/пробел)
Живые клетки - "*"

Кастомная клетка - "X"
"""

"""
Кастомная клетка и условия для неё:

Если ячейка имеет тип 2 и имеет менее двух соседей типа 2, она превращается в ячейку типа 0.
Если ячейка имеет тип 2 и имеет более 3 соседей типа 2, она превращается в ячейку типа 0.
Если ячейка относится к типу 2 и имеет двух или трех соседей типа 2, она остается ячейкой типа 2.
Если ячейка не относится к типу 2 и имеет ровно трех соседей типа 2, она превращается в ячейку типа 2.
"""


def create_board(n, m):
    board = [[random.randint(0, 2) for i in range(m)] for j in range(n)]
    return board

def print_board(board):
    for row in board:
        print(" ".join(["*" if cell == 1 else " " if cell == 0 else "X" for cell in row]))
    print("\n")

def get_next_state(board):
    n = len(board)
    m = len(board[0])
    new_board = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            live_neighbors_1 = 0
            live_neighbors_2 = 0
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if x == 0 and y == 0:
                        continue
                    if i + x < 0 or i + x >= n or j + y < 0 or j + y >= m:
                        continue
                    if board[i + x][j + y] == 1:
                        live_neighbors_1 += 1
                    elif board[i + x][j + y] == 2:
                        live_neighbors_2 += 1
            if board[i][j] == 1:
                if live_neighbors_1 < 2 or live_neighbors_1 > 3:
                    new_board[i][j] = 0
                else:
                    new_board[i][j] = 1
            elif board[i][j] == 2:
                if live_neighbors_2 < 2 or live_neighbors_2 > 3:
                    new_board[i][j] = 0
                else:
                    new_board[i][j] = 2
            else:
                if live_neighbors_2 == 3:
                    new_board[i][j] = 2
                else:
                    new_board[i][j] = board[i][j]
    return new_board

def is_game_over(board, prev_boards):
    flat_board = [cell for row in board for cell in row]
    flat_prev_boards = [[cell for row in prev_board for cell in row] for prev_board in prev_boards]
    return sum(flat_board) == 0 or flat_board in flat_prev_boards

def play_game(n, m):
    board = create_board(n, m)
    prev_boards = []
    while not is_game_over(board, prev_boards):
        print_board(board)
        prev_boards.append(board)
        board = get_next_state(board)
        time.sleep(1)

play_game(10,10)
