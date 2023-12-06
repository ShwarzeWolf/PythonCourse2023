import time


def log_exec_time(func):
    """ Decorator to log execution time of function. """
    time_format = "%H:%M:%S"

    def wrapper():
        starting_time = time.time()
        print(f" LOG: {func.__name__}() started executing at {time.strftime(time_format)}")

        result = func()

        ending_time = time.time()
        print(f" LOG: {func.__name__}() ended executing at {time.strftime(time_format)}")

        print(f" LOG: time for {func.__name__}() to execute is {ending_time - starting_time} seconds")

        return result

    return wrapper


@log_exec_time
def test_1():
    print('counting')
    time.sleep(2)
    print("result is 10")
    return 10


@log_exec_time
def test_2():
    _sum = 0
    current_num = 0

    while current_num <= 100000000:
        _sum += current_num
        current_num += 1
    
    return _sum


@log_exec_time
def test_3():
    return sum(range(0, 100000001))


@log_exec_time
def test_4():
    s = 0
    for i in range(0, 100000001):
        s += i
    return s


if __name__ == '__main__':
    test_flags = input("Choose tests (1-4): ")

    if "1" in test_flags:
        print("TEST 1")
        print(test_1())
        print()

    if "2" in test_flags:
        print("TEST 2")
        print(test_2())
        print()

    if "3" in test_flags:
        print("TEST 3")
        print(test_3())
        print()

    if "4" in test_flags:
        print("TEST 4")
        print(test_4())
        print()
    
