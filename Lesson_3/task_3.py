def my_func(a, b, c):
    """Сумма двух наибольших агрументов"""

    try:
        my_list = [a, b, c]
        my_list.remove(min(my_list))
        result = my_list[0] + my_list[1]
        return result
    except:
        err = 'Что-то пошло не так, проверьте тип аргументов'
        return err


print(my_func(2, 4, 'п'))
print(my_func(2, 4, 6))
