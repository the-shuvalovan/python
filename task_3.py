n = int(input('Введите число от 1 до 9: '))
if n < 1 or n > 9:
    raise Exception('Число должно быть от 1 до 9')
else:
    n = str(n)
    nnn = int((n.rjust(3, n)))
    nn = int((n.rjust(2, n)))
    n = int(n)
print(n + nn + nnn)