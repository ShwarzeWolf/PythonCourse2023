def sum_square(*args):
    sum_sq = 0
    for digit in args:
        if not isinstance(digit, (int, float)):
            print('Error')
            return None
        sum_sq += digit ** 2
    return sum_sq


sum_sq = sum_square(1, 2, 3, '')
if sum_sq is not None:
    print(sum_sq)
