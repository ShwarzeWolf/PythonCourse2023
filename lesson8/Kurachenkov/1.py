def sum_of_squares(*args):
    """
    Вычисляет сумму квадратов заданных аргументов.

    Аргументы:
        *args: аргументы, для которых нужно вычислить сумму квадратов.

    Возвращается:
        int: Сумма квадратов заданных аргументов.
    """
    return sum(arg**2 for arg in args)