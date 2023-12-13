import time

def repeat_with_delay(n,t):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
                time.sleep(t)
        return wrapper
    return decorator

@repeat_with_delay(15, 0.75)
def print_hello():
    print("Hello, world!")

print_hello()
