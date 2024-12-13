import time
def timer(f):
    def decorator(*args, **kwargs):
        start = time.perf_counter()
        result = f(*args, **kwargs)
        end = time.perf_counter()
        print(f"Время старта: {start}")
        print(f"Время финиша: {end}")
        print(f"Время выполнения: {end - start}")
        return result
    return decorator

@timer
def amount(n):
    count = 0
    for i in range(1, n + 1):
        count += 1
    return count

print(amount(12))