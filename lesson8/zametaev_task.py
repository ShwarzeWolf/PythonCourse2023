#Задание 1
def sum_number(*lst):
    summa = 0
    for i in lst:
        a = i ** 2
        summa += a
    return summa


#Задание 2
def check_numbers(*args):
    for i in args:
        if not isinstance(i, (int, float)):
            print("ERRORRRRRRRRRRRR")
            return None
    return None
print(check_numbers(1,2,"3"))

#Задание 3
strings = list()

upper_strings = list(map(lambda x: x.upper(), strings))


#Задание 4
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)