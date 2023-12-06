import copy
import random

n = 5
m = 5
field = [[random.randint(0, 1) for x in range(n)] for y in range(m)]

while True:
    for row in field:
        print(*row)
    print()

    if sum([sum(row) for row in field]) == 0:
        print('Game over')
        break

    next_field = copy.deepcopy(field)
    for y in range(n):
        for x in range(m):
            neighbors_coordinates = [
                (x - 1, y - 1),
                (x - 1, y),
                (x - 1, y + 1),
                (x, y - 1),
                (x, y + 1),
                (x + 1, y - 1),
                (x + 1, y),
                (x + 1, y + 1),
            ]
            existing_neighbours = [coord for coord in neighbors_coordinates if 0 <= coord[0] < m and 0 <= coord[1] < n]
            num_of_neighbours = 0
            for i, j in existing_neighbours:
                num_of_neighbours += field[i][j]

            if num_of_neighbours == 3 and field[x][y] == 0:
                next_field[x][y] = 1
                continue

            if (num_of_neighbours < 2 or num_of_neighbours > 3) and field[x][y] == 1:
                next_field[x][y] = 0
                continue

    field = next_field
    input()
