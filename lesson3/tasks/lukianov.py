import math

print('1 - Squares of figures')
print('2 - Palindrome')
task = input('Choose task: ')

if task == '1':
    n = int(input('Number of figures: '))

    c = 0
    s_sum = 0

    for i in range(n):
        figure = input('Enter figure: ').lower()
        s = 0
        if figure == 'square':
            a = float(input('Enter side length: '))
            s = a ** 2
            c += 1
        elif figure == 'circle':
            r = float(input('Enter radius: '))
            s = 2 * math.pi * r
            c += 1
        elif figure == 'rectangle':
            a = float(input('Enter length: '))
            b = float(input('Enter width: '))
            s = a * b
            c += 1
        else:
            print('Unknown figure')
        s_sum += s

    print(f'Number of figures counted: {c}')
    print(f'Sum of squares: {s_sum}')

elif task == '2':
    word = input('Enter word: ')
    w1 = word.lower()
    w2 = word.lower()[::-1]

    for i in range(len(w1) // 2):
        if w1[i] != w2[i]:
            print('NO')
            break
    else:
        print('YES')