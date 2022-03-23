list = []
names = []
prices = []
number = []
n = int(input('Сколько товаров вы хотите добавить? '))
x = 1
for i in range(n):
    a = input('Введите название товара: ')
    b = input('Введите стоимость товара: ')
    c = input('Введите количество товара в наличии (шт): ')
    names.append(a)
    prices.append(b)
    number.append(c)
    mydict = dict(название=a, цена=b, количество=c)
    mytuple = (x, mydict)
    list.append(mytuple)
    x += 1
print(list)
names_dict = dict(Названия=names, Цены=prices, Количество=number)
print(names_dict)