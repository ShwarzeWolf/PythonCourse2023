import random
import time

# n = int(input("Enter width: "))
# m = int(input("Enter height: "))


n = 7
m = 7
board = [[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 1, 1, 0, 0],
         [0, 0, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0]]
# board = [[random.randint(0, 1) for _ in range(n)] for _ in range(m)]
next_board = board

# n = 4
# m = 4
# board = [[0, 1, 0, 0],
#          [0, 1, 0, 0],
#          [0, 1, 0, 0],
#          [0, 0, 0, 0]]

while 1:
    print("\n"*20)
    for y in range(m):
        for x in range(n):
            # print("#" if board[y][x] == 1 else " ", end="")
            print(board[y][x], end="")
        print()

    for y in range(m):
        for x in range(n):
            counter = 0
            for i in [y-1, y, 0 if y+1 == m else y+1]:
                for j in [x-1, x, 0 if x+1 == n else x+1]:
                    if board[i][j] == 1 and not (i == y and j == x):
                        counter += 1
                        if y == 2 and x == 2:
                            print(f"Neighbour at {i}:{j}")
            print(f"board{x}:{y} has {counter}")

            if (counter == 2 or counter) == 3 and board[y][x]:
                continue
            if counter == 3 and board[y][x] == 0:
                next_board[y][x] = 1
                print(f"New cell at {x}:{y}")
                continue
            if (counter < 2 or counter > 3) and board[y][x] == 1:
                next_board[y][x] = 0
                print(f"Cell died at {x}:{y}")
                continue

            # if board[y][x] == 1:
            #     if counter < 2 or counter > 3:
            #         board[y][x] = 0
            #         print(f"Cell died at {x}:{y}")
            #     elif counter == 2 or counter == 3:
            #         board[y][x] = 1
            # else:
            #     if counter == 3:
            #         board[y][x] = 1
            #         print(f"New cell at {x}:{y}")
    print("Next board: \n")
    for y in range(m):
        for x in range(n):
            print(next_board[y][x], end="")
        print()
    time.sleep(1)
    board = next_board
