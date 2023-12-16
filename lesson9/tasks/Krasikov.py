import time


def time_decorator(func):
    def wrapper():
        start = round(time.time(), 3)
        print(f"Started at: {time.strftime('%H:%M:%S')}")
        func()
        finish = round(time.time(), 3)
        print(f"Finished at: {time.strftime('%H:%M:%S')}")
        print(f"Duration: {round(finish - start, 2)} seconds")
    return wrapper


@time_decorator
def my_func():
    print("Function started")
    time.sleep(1)
    print("Function stopped")


my_func()