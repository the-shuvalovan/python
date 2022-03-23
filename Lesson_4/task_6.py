from itertools import count
from itertools import cycle


def my_func_1(x, y):
    l = []
    for n in count(x):
        if n > y:
            return l
        else:
            l.append(n)
            print(n)


def my_func_2(k, l):
    z = 0
    i = len(l) * (k-1)
    result = []
    for m in cycle(l):
        if z == i:
            return result
        result.append(m)
        print(m)
        z += 1


a = int(input('С какого числа начнем перечисление? '))
b = int(input('На каком числе закончим? '))
c = int(input('Сколько раз повторить перечисление? '))

my_list = my_func_1(a, b)
my_func_2(c, my_list)
