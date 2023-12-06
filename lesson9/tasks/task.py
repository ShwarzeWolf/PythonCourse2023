import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print("Начало:", start_time)
        print("Конец:", end_time)
        print("Время выполнения:", execution_time, "секунд")
        return result
    return wrapper