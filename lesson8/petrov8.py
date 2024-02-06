def sum_sqare(*args):
    sum_ = 0
    for i in args:
        if isinstance(i, int) or isinstance(i, float):
            sum_ += i**2
        else:
            return None
    return sum_
print(sum_sqare(1, 2, "3"))

In = ["ПрИвЕт", "миР"]
Out = list(map(lambda x: x.upper(), In))
print(Out)

def recursion(n):
    if n > 1:
        return n*recursion(n-1)
    else:
        return n

print(recursion(4))