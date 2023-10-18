from random import randint

a = []
for i in range(100):
    a.append(randint(1, 100))

print(sum(a))