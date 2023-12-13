import time

def number_of_times(n=1, t=3):
    def wrapper1(func):
        def wrapper2(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
                time.sleep(t)
        return wrapper2
    return wrapper1

@number_of_times(5, 2)
def just_func():
    print("just func")

just_func()