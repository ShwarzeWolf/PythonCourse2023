import random
import time

"""
Мёртвые клетки - " " (пустота/пробел)
Живые клетки - "*"
"""

def create_board(n, m):
    board = [[random.randint(0, 1) for i in range(m)] for j in range(n)]
    return board

play_game(5, 5)
