import random
import time

"""
Мёртвые клетки - " " (пустота/пробел)
Живые клетки - "*"
"""

def create_board(n, m):
    board = [[random.randint(0, 1) for i in range(m)] for j in range(n)]
    return board

def print_board(board):
    for row in board:
        print(" ".join(["*" if cell == 1 else " " for cell in row]))
    print("\n")

def get_next_state(board):
    """
    Вычисляет следующее состояние игрового поля.

    Аргументы:
        board (list): Текущее состояние игрового поля.

    Возвращает:
        list: Следующее состояние игрового поля.
    """
    n = len(board)
    m = len(board[0])

    # Создаем новую доску с теми же размерами, что и текущая доска
    new_board = [[0 for i in range(m)] for j in range(n)]

    # Перебираем каждую клетку на доске
    for i in range(n):
        for j in range(m):
            live_neighbors = 0

            # Перебираем соседние клетки
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    # Пропускаем текущую клетку
                    if x == 0 and y == 0:
                        continue

                    # Пропускаем клетки, выходящие за границы доски
                    if i + x < 0 or i + x >= n or j + y < 0 or j + y >= m:
                        continue

                    # Подсчитываем живые соседние клетки
                    if board[i + x][j + y] == 1:
                        live_neighbors += 1

            # Применяем правила игры
            if board[i][j] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    new_board[i][j] = 0
                else:
                    new_board[i][j] = 1
            else:
                if live_neighbors == 3:
                    new_board[i][j] = 1
                else:
                    new_board[i][j] = 0

    return new_board

def is_game_over(board, prev_boards):
    """
    Проверяет, окончена ли игра.

    Аргументы:
    - board: текущая доска игры
    - prev_boards: список предыдущих досок игры

    Возвращает:
    - True, если игра окончена, иначе False
    """
    # Преобразовать доску и предыдущие доски в одномерные списки
    flat_board = [cell for row in board for cell in row]
    flat_prev_boards = [[cell for row in prev_board for cell in row] for prev_board in prev_boards]
    
    # Проверить, равны ли сумма элементов доски и сумма элементов предыдущих досок
    # Или доска содержится в списке предыдущих досок
    return sum(flat_board) == 0 or flat_board in flat_prev_boards
def play_game(n, m):
    """
    Запускает игру.
    
    Аргументы:
    n (int): Количество строк на игровом поле.
    m (int): Количество столбцов на игровом поле.

    Возвращает:
    None
    """
    # Создание игрового поля
    board = create_board(n, m)
    
    # Список предыдущих состояний игрового поля
    prev_boards = []
    
    # Пока игра не закончена
    while not is_game_over(board, prev_boards):
        # Вывод текущего состояния игрового поля
        print_board(board)
        
        # Добавление текущего состояния в список предыдущих состояний
        prev_boards.append(board)
        
        # Получение следующего состояния игрового поля
        board = get_next_state(board)
        
        # Задержка на 1 секунду
        time.sleep(1)

play_game(5, 5)
