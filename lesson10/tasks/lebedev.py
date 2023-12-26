from time import sleep


def repeat_delay(repeats_count=1, delay=0.0):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(repeats_count):
                print(f"{func.__name__}() executed for the {i + 1} time")
                result = func(*args, **kwargs)
                sleep(delay)
            return result
        return wrapper
    return decorator


@repeat_delay(3, 2)
def _sum(a, b):
    return a + b

x = _sum(1, 2)
print("sum = {sum}".format(sum=x))
