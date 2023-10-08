# Начианем с того, что такое переменная
name = 'Kristina'
index = 0

# Какие из этих имен - валидные имена?
# 100_lessons = 100
# ?questions? = 200
# _some_underscore_value = 2
# while = 10

# начиная с версии 3 работает и такое чудо
имя_кошки = 'Ежевика'
print(имя_кошки)

### Основные типы данных
### Вопрос - какие типы данных вы знаете?
### Main data types: ...
### задание: написать программу, которая будет считать площадь треугольника по длинам его сторон

### Tell about numbers
# step 1
a = 3
b = 4

square = 0.5 * a * b
print(square)

# step 2
a = 3
b = 4
c = 6

p = (a + b + c) / 2.0
square = ((p - a) * (p - b) * (p - c) * p) ** 0.5

print(square)

# Рассказать про условные операторы и свойства bool
# step 3
a = 3
b = 4
c = 100

if a + b > c:
    p = (a + b + c) / 2.0
    square = ((p - a) * (p - b) * (p - c) * p) ** 0.5

    print(square)
else:
    print('Defined lengths could not form a square')

# step 4
a = 3
b = 4
c = 0.5

if a + b > c and a + c > b and c + b > a:
    p = (a + b + c) / 2.0
    square = ((p - a) * (p - b) * (p - c) * p) ** 0.5

    print(square)
else:
    print('Defined lengths could not form a square')

# step 5
a = 0
b = 0
c = 0

if a <= 0 and b <= 0 and c <= 0:
    print('Triangle sizes could not be with negative lengths')
elif a + b > c and a + c > b and c + b > a:
    p = (a + b + c) / 2.0
    square = ((p - a) * (p - b) * (p - c) * p) ** 0.5

    print(square)
else:
    print('Defined lengths could not form a square')

# step 5
a = float(input('Enter first side length: '))
b = float(input('Enter second side length: '))
c = float(input('Enter third side length: '))

if a <= 0 and b <= 0 and c <= 0:
    print('Triangle sizes could not be with negative lengths')
elif a + b > c and a + c > b and c + b > a:
    p = (a + b + c) / 2.0
    square = ((p - a) * (p - b) * (p - c) * p) ** 0.5

    print(square)
else:
    print('Defined lengths could not form a square')
    

# step 6
a, b, c = map(float, input().split(' '))

if a <= 0 and b <= 0 and c <= 0:
    print('Triangle sizes could not be with negative lengths')
elif a + b > c and a + c > b and c + b > a:
    p = (a + b + c) / 2.0
    square = ((p - a) * (p - b) * (p - c) * p) ** 0.5

    print(square)
else:
    print('Defined lengths could not form a square')

# step 7
number_of_triaangles = 3

for i in range(3):
    a, b, c = map(float, input().split(' '))

    if a <= 0 and b <= 0 and c <= 0:
        print('Triangle sizes could not be with negative lengths')
    elif a + b > c and a + c > b and c + b > a:
        p = (a + b + c) / 2.0
        square = ((p - a) * (p - b) * (p - c) * p) ** 0.5

        print(square)
    else:
        print('Defined lengths could not form a square')
else:
    print(f'{number_of_triaangles} squares calculated')