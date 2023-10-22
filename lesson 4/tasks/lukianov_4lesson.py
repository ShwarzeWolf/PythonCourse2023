from random import randint
from turtle import *

print('Task 1')
print('___________')

rand_list = []
for i in range(100):
    rand_list.append(randint(1, 100))
print(f'Sum of random list: {sum(rand_list)}')
print('___________')

print('Task 2')
print('___________')

double_list = list(map(int, input('Enter list: ').split()))

while True:
    check_number = double_list[0]
    double_list.pop(0)
    if check_number in double_list:
        double_list.remove(check_number)
    else:
        print(f'Single number: {check_number}')
        break
print('___________')

print('Task 3')
print('___________')

telephone_book = dict()
telephone_book['Mom'] = '+1(111)111-11-11'
telephone_book['Dad'] = '+2(222)222-22-22'
telephone_book['Brother'] = '+3(333)333-33-33'

for name, telephone_number in telephone_book.items():
    print(f'{name}: {telephone_number}')

t = Turtle()
for i in range(360):
    t.fd(2)
    t.right(1)

t.screen.mainloop()
