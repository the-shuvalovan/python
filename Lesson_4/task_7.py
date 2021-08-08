def fact(n):
    f = 1
    for i in range(2, n + 1):
        yield f
        f *= i
    yield f
    return f


n = int(input('Введите число: '))
fact(n)
for el in fact(n):
    print(el)
