def func(x,y):
    """Деление чисел"""

    if y == 0:
        print('Деление на ноль невозможно')
    else:
        a = x / y
        return(round(a,2))

print(func((int(input('Введите первое число: '))),int(input('Ввелите второе число: '))))
