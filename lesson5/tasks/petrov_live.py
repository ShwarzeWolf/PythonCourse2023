from time import sleep
import copy

field = [[]]
field_file = open("PythonCourse2023/lesson5/tasks/field_of_live.txt", "r", encoding="utf-8")
field_raw = field_file.read()

index = 0
for i in field_raw:
    if i == "0" or i == "1":
        field[index].append(int(i))
    elif i == "e":
        field.append([])
        index += 1

#print(field)

"""
field = [[0,0,0,0,0,0,0,0,0,],
         [0,0,0,0,1,0,0,0,0,],
         [0,0,0,0,1,0,0,0,0,],
         [0,0,0,0,1,0,0,0,0,],
         [0,0,0,0,0,0,0,0,0,],]
"""

run = True
while run:
    new_field = copy.copy(field)
    fixes = []
    for y in range(len(field)):
        for x in range(len(field[y])):
            cell = new_field[y][x]
            print(cell, end="")

            try:
                neighbours = [field[y][x+1],
                            field[y+1][x+1],
                            field[y+1][x],
                            field[y+1][x-1],
                            field[y][x-1],
                            field[y-1][x-1],
                            field[y-1][x],
                            field[y-1][x+1],]
            except:
                if x == len(field[y])-1 and y == len(field)-1:
                    neighbours = [field[y][0],
                                field[0][0],
                                field[0][x],
                                field[0][x-1],
                                field[y][x-1],
                                field[y-1][x-1],
                                field[y-1][x],
                                field[y-1][0],]
                elif y == len(field)-1:
                    neighbours = [field[y][x+1],
                            field[0][x+1],
                            field[0][x],
                            field[0][x-1],
                            field[y][x-1],
                            field[y-1][x-1],
                            field[y-1][x],
                            field[y-1][x+1],]
                elif x == len(field[y])-1:
                    neighbours = [field[y][0],
                                field[y+1][0],
                                field[y+1][x],
                                field[y+1][x-1],
                                field[y][x-1],
                                field[y-1][x-1],
                                field[y-1][x],
                                field[y-1][0],]
            
            alive_neighbour = 0
            for neighbour in neighbours:
                if neighbour == 1:
                    alive_neighbour += 1
            
            if cell == 1 and (alive_neighbour == 0 or alive_neighbour == 1 or alive_neighbour > 3): #если у живой клетки 0-1 или >3 живых соседей
                fixes.append([y, x])
            elif cell == 0 and (alive_neighbour == 3): #если у мертвой клетки ровно 3 живых соседа
                fixes.append([y, x])

        print()
    print("/"*len(field[0]))
    for fix in fixes:
        if field[fix[0]][fix[1]] == 0:
            field[fix[0]][fix[1]] = 1
        elif field[fix[0]][fix[1]] == 1:
            field[fix[0]][fix[1]] = 0
        
    try:
        sleep(1)
    except KeyboardInterrupt:
        print("exit")
        sleep(1)
        run = False