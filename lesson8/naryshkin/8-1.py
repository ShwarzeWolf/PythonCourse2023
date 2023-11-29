def sum_of_squares(*args):
    return sum(arg ** 2 for arg in args)
print(sum_of_squares(2, 5))