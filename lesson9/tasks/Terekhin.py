def func_time(func):
    import time

    def time_counter():
        st_time = round(time.time(), 2)
        func()
        f_time = round(time.time() - st_time, 2)
        print(f'Время старта исполнения функции - {st_time} с')
        print(f'Время финиша исполнения функции - {round(time.time(), 2)} с')
        print(f'Время исполнения функции - {f_time} с')
    return time_counter


@func_time
def some_func():
    for x in range(10**8):
        if x * 2 == -1:
            print('Error')
    print('All right!')


some_func()
