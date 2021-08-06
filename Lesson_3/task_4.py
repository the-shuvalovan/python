def my_func(x, y):
    """Возведение числа x в степень y, первый способ"""

    if x == 0:
        print('Деление на ноль невозможно')
    elif y == 0:
        return 1
    else:
        result = (x ** y)
        return result

print(my_func((int(input('Введите первое число (действительное положительное): '))),int(input('Введите второе число (целое отрицательное): '))))

def my_func_2(x, y):
    """Возведение числа x в степень y, второй способ"""

    if x == 0:
        print('Деление на ноль невозможно')
    elif y == 0:
        return 1
    else:
        a = abs(y)-1
        b = x
        for i in range(a):
            b = (b * x)
        result = 1/b
        return result

print(my_func_2((int(input('Введите первое число (действительное положительное): '))),int(input('Введите второе число (целое отрицательное): '))))