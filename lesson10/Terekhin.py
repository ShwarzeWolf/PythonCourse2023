import time


def repeat(count=2, pause_time=0.5):
    def func_repeat(func):
        def repeat_wrapper():
            for i in range(count):
                func()
                time.sleep(pause_time)

        return repeat_wrapper

    return func_repeat


@repeat(4, 1.5)
def some_func():
    print('Function executed!')


some_func()
