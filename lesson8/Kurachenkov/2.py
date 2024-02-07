def sum_of_squares(*args):
    """
    Вычисляет сумму квадратов заданных чисел.

    Аргументы:
        *args: числа, для которых необходимо вычислить квадраты.

    Возвращается:
        Сумма квадратов заданных чисел.

    Повышения:
        none.
    """
    for arg in args:
        if not isinstance(arg, (int, float)):
            print("Error: All arguments must be numbers.")
            return None
    return sum(arg**2 for arg in args)