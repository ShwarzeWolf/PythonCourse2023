import time

def decorator(n, t):
    def function(func):
        def wrapper():
            for i in range(n):
                func()
                time.sleep(t)
        return wrapper
    return function

@decorator(5, 3)
def test():
    print("HI")

test()