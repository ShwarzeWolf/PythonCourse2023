import time

def show_time_func(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"start time - {start_time}, end time - {end_time}")
    return wrapper()


@show_time_func
def just_func():
    print("func is starting")
    time.sleep(1)
    print("func is stopping")

just_func()
