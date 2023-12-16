print('TASK 1')


def square_sum(*args, **kwargs):
    summary = 0

    for number in args:
        if type(number) == int or type(number) == float:
            summary += number ** 2

    for number in kwargs.values():
        if type(number) == int or type(number) == float:
            summary += number ** 2

    return summary


print(square_sum(1, 'f', 2, a=5, fg=7, c='hdsa'))

print('_________')
print('TASK 2')


def is_all_number(*args, **kwargs):
    for number in args:
        if not (type(number) == int or type(number) == float):
            return f'Error: {number} is not a number'

    for number in kwargs.values():
        if not (type(number) == int or type(number) == float):
            return f'Error: {number} is not a number'

    return None


print(is_all_number(1, 2.34, 3, a=89, b='fg', gfh='3457.7354'))

print('_________')
print('TASK 3')

words = 'I am so tired'.split()
print(words)
words = list(map(lambda word: word.upper(), words))
print(words)

print('_________')
print('TASK 4')


def fact(n):
    if n == 1:
        return 1
    return fact(n - 1) * n


print(fact(6))
