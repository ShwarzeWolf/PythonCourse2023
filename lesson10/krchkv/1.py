import time

def repeat_with_delay(n, t):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
                time.sleep(t)
            return result
        return wrapper
    return decorator

@repeat_with_delay(n=5, t=2)
def my_function():
    print("Function is running")

my_function()