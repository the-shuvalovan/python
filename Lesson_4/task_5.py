from functools import reduce


def my_func(a, b):
    return a * b


my_list = [n for n in range(100, 1002, 2)]
result = reduce(my_func, my_list)
