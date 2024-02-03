import time


def repeat(count=2, pause_time=0.5):
    def func_repeat(func):
        def repeat_wrapper(*args, **kwargs):
            for i in range(count):
                func(*args, **kwargs)
                time.sleep(pause_time)

        return repeat_wrapper

    return func_repeat


@repeat(4, 1.5)
def some_func(*args, **kwargs):
    print(f'Function executed!\nArgs: {args}\nKwargs: {kwargs}')


some_func(1, 'something', numder=15)
