my_list = [7, 5, 3, 3, 2]
n = int(input('Введите натуральное число: '))
m = 0
if n>0:
    if n > my_list[0]:
        my_list.insert(0,n)
    elif n<= my_list[-1]:
        my_list.append(n)
    else:
        while my_list[m] >= n:
            m+=1
        my_list.insert(m,n)
    print(my_list)
else: print('Вы ввели не натуральное число')