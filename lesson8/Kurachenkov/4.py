def factorial(n):
    """
    Вычисляет факториал заданного числа.

    Параметры:
        n (int): число, для которого вычисляется факториал.

    Возвращается:
        int: Факториал данного числа.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)