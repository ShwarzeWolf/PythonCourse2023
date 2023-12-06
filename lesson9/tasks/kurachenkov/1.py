import time

def exec_time_decortr(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Функция {func.__name__} началась в {start_time}")
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Функция {func.__name__} закончила работу в {end_time}")
        print(f"Время выполнения: {end_time - start_time}")
        return result
    return wrapper


# пример

@exec_time_decortr
def test2():
    time.sleep(1)

test2()