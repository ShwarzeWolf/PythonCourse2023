def task1(*args):
    return sum([i**2 for i in args])


def task2(*args):
    res = 0
    for i in args:
        if type(i) == int:
            res += i**2
        else:
            print("Error")
            return None
    return res


arr = ["hello", "ByE"]
print(list(map(lambda string: string.upper(), arr)))


def task4(a):
    if a > 1:
        return task4(a-1)*a
    else:
        return a