import random
import turtle
import time
# Задание 1
array = []
for i in range(100):
    array.append(random.randint(0, 1000))
print(array)
sum = sum(array)
print(sum)


# Задание 2
array = input().split(", ")
for i in range(len(array)):
    array[i] = int(array[i])
for i in array:
    counter = 0
    for a in array:
        if a == i:
            counter += 1
            if counter == 2:
                break
    else:
        print(i)


# Задание 3
phones = {"12345": ["Friend", "Moscow"], "67890": ["Mum", "Saint-Petersburg"], "13579": ["Dad", "Saint-Petersburg"]}
for number, data in phones.items():
    print(f"Phone: {number}, name: {data[0]}, location: {data[1]}")


# Задание 4
for i in range(360):
    turtle.forward(3)
    turtle.right(1)
time.sleep(1)
