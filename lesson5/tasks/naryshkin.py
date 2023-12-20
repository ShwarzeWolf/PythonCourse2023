import random
import time


def create_field(n, m):
    field = []
    for i in range(n):
        field.append([random.randint(0, 1) for j in range(m)])
    return field


def draw_field(field):
    for row in field:
        print("".join(["1" if cell == 1 else " " for cell in row]))


def new_generation(field):
    new_field = []
    for i in range(len(field)):
        new_row = []
        for j in range(len(field[0])):
            neighbors = count_neighbors(field, i, j)
            if field[i][j] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_row.append(0)
                else:
                    new_row.append(1)
            else:
                if neighbors == 3:
                    new_row.append(1)
                else:
                    new_row.append(0)
        new_field.append(new_row)
    return new_field


def count_neighbors(field, i, j):
    neighbors = 0
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if x < 0 or x >= len(field) or y < 0 or y >= len(field[0]):
                continue
            if field[x][y] == 1:
                neighbors += 1
    return neighbors


def main():
    n = 10
    m = 10
    field = create_field(n, m)
    draw_field(field)
    while True:
        new_field = new_generation(field)
        draw_field(new_field)
        print("----------")
        if field == new_field:
            if time.time() - start_time > 3:
                break
        field = new_field
        time.sleep(0.5)


if __name__ == "__main__":
    start_time = time.time()
    main()
