import time


def time_decoration(func):
    start_time_in_secs = time.time()
    start_time = time.ctime(start_time_in_secs)
    print(f'start time: {start_time}')

    func()

    end_time_in_secs = time.time()
    end_time = time.ctime(end_time_in_secs)
    print(f'end time: {end_time}')

    print(f'function duration: {end_time_in_secs - start_time_in_secs}secs')

@time_decoration
def print_from_1_to_1000():
    for number in range(1, 1001):
        print(number)


