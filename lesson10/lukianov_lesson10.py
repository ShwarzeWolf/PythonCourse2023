import time


def func_decorator(n=3, delay=1):
    def func_wrapping(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                print(f'Print number {i + 1}')
                print(func(*args, **kwargs))
                print('')
                time.sleep(delay)

        return wrapper

    return func_wrapping


@func_decorator(3, 1)
def sum_of_cubes(a, b):
    s = 0
    for number in range(a, b + 1):
        s += number ** 3
    return s


sum_of_cubes(1, 5)
