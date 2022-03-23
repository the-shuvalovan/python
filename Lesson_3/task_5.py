x = 0
a = 0

while x != "q":
    print("Для выхода их программы - q")
    mylist = input('Введите строку чисел, разделенных пробелом: ')
    my_list = mylist.split()
    x = my_list[-1]
    try:
        for i in my_list:
            a += int(i)
        print(a)
    except ValueError:
        if x == "q":
            print(a)
        else:
            print(f'Что-то пошло не так, введен неверный элемент. Но введенные числа были суммированы: {a}')
else:
    print("Вы вышли из программы")
