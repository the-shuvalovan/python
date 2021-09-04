storage = {'hp': ['Количество: 10 шт.', ['Printer', 1000, False, False]], 'Cannon': ['Количество: 5 шт.', ['Scanner', 2000, False, True]]}
store1 = {}
store2 = {'WorkCentre': ['Количество: 3 шт.', ['Xerox', 5000, True, True]]}
store3 = {}

class Storage:
    def __init__(self, capacity):
        self.capacity = capacity

    @staticmethod
    def store(obj):
        storage.update({obj.name: [f'Количество: {obj.number} шт.', obj.params]})

    @staticmethod
    def shipped_1(obj, n):
        left = obj.number - n
        if left < 0:
            print(f'Товара в таком количестве нет, остаток: {obj.number}')
        elif left == 0:
            store1.update({obj.name: [f'Количество: {n} шт.', obj.params]})
            storage.__delitem__(obj.name)
            print('Отгрузка произведена, на складе товара не осталось')
        else:
            store1.update({obj.name: [f'Количество: {n} шт.', obj.params]})
            storage.update({obj.name: [f'Количество: {left} шт.', obj.params]})
            print(f'Отгрузка произведена, на складе товара не осталось {left} единиц.')

    @staticmethod
    def shipped_2(obj, n):
        left = obj.number - n
        if left < 0:
            print(f'Товара в таком количестве нет, остаток: {obj.number}')
        elif left == 0:
            store2.update({obj.name: [f'Количество: {n} шт.', obj.params]})
            storage.__delitem__(obj.name)
        else:
            store2.update({obj.name: [f'Количество: {n} шт.', obj.params]})
            storage.update({obj.name: [f'Количество: {left} шт.', obj.params]})

    @staticmethod
    def shipped_3(obj, n):
        left = obj.number - n
        if left < 0:
            print(f'Товара в таком количестве нет, остаток: {obj.number}')
        elif left == 0:
            store3.update({obj.name: [f'Количество: {n} шт.', obj.params]})
            storage.__delitem__(obj.name)
        else:
            store2.update({obj.name: [f'Количество: {n} шт.', obj.params]})
            storage.update({obj.name: [f'Количество: {left} шт.', obj.params]})


class Goods:
    def __init__(self, name, number, price):
        self.name = name
        self.number = number
        self.price = price


class Printer(Goods):
    def __init__(self, name, number, price):
        super().__init__(name, number, price)
        self.type = 'Printer'
        self.c = input('Принтер цветной? (y/n) ')
        if self.c == 'y' or self.c == 'Y':
            self.color = True
        elif self.c == 'n' or self.c == 'N':
            self.color = False
        self.l = input('Печать лазерная? (y/n) ')
        if self.l == 'y' or self.c == 'Y':
            self.laser = True
        elif self.l == 'n' or self.c == 'N':
            self.laser = False
        self.params = [self.type, self.price, self.color, self.laser]


class Scanner(Goods):
    def __init__(self, name, number, price, industrial=False, net=False):
        super().__init__(name, number, price)
        self.type = 'Scanner'
        self.industrial = industrial
        self.net = net
        self.params = [self.type, self.price, self.industrial, self.net]


class Xerox(Goods):
    def __init__(self, name, number, price, color=False, net=False):
        super().__init__(name, number, price)
        self.type = 'Xerox'
        self.color = color
        self.net = net
        self.params = [self.type, self.price, self.color, self.net]

x=0
while x != "q":
    print("Добавить товар на склад - 1. Отгрузить товар в магазин - 2. Посмотреть остатки - 3. Выход - q.")
    x = input('Ввод: ')
    if x == '3':
        print(f'Остаток на складе: {storage}')
        print(f'Остаток на магазине 1: {store1}')
        print(f'Остаток на магазине 2: {store2}')
        print(f'Остаток на магазине 3: {store3}')
    elif x == '1':
        try:
            name = input('Введите название товара: ')
            price = int(input('Введите стоимость единицы: '))
            number = int(input('Сколько единиц добавить на склад? '))
            product = input('Введите тип товара. Принтер - 1, сканер - 2, ксерокс - 3 ')
            if int(product) == 1:
                a = Printer(name, number, price)
                Storage.store(a)
                print('Товар заведен')
            elif int(product) == 2:
                a = Scanner(name, number, price)
                Storage.store(a)
                print('Товар заведен')
            elif int(product) == 3:
                a = Xerox(name, number, price)
                Storage.store(a)
                print('Товар заведен')
            else: print('Неизвестная команда')
        except: print('Ошибка во введенных данных')
    elif x == '2':
        print(f'Сейчас на складе: {storage}')
        name = input('Введите название товара, который нужно отгрузить: ')
        try:
            data = storage.get(name)
            params = data[1]
            price = params[1]
            t = params[0]
            param1 = params[2]
            param2 = params[3]
            n = data[0]
            n1 = n.split(' ')
            n2 = n1[1]
            num = int(n2)
            number = int(input('Введите количество товара, который нужно отгрузить: '))
            if t == 'Printer':
                print('Сверим данные о товаре:')
                a = Printer(name, num, price)
                s = input('Введите номер магазина, на который нужно отгрузить (1, 2 или 3): ')
                if s == '1':
                    Storage.shipped_1(a, number)
                elif s == '2':
                    Storage.shipped_2(a, number)
                elif s == '3':
                    Storage.shipped_3(a, number)
                else: print('Магазина с таким номером нет')
            elif t == 'Scanner':
                print('Сверим данные о товаре:')
                a = Scanner(name, num, price)
                s = input('Введите номер магазина, на который нужно отгрузить (1, 2 или 3): ')
                if s == '1':
                    Storage.shipped_1(a, number)
                elif s == '2':
                    Storage.shipped_2(a, number)
                elif s == '3':
                    Storage.shipped_3(a, number)
                else: print('Магазина с таким номером нет')
            else:
                print('Сверим данные о товаре:')
                a = Xerox(name, num, price)
                s = input('Введите номер магазина, на который нужно отгрузить (1, 2 или 3): ')
                if s == '1':
                    Storage.shipped_1(a, number)
                elif s == '2':
                    Storage.shipped_2(a, number)
                elif s == '3':
                    Storage.shipped_3(a, number)
                else: print('Магазина с таким номером нет.')
        except: print('Введены некорректные данные.')
    else:
        print('Неизвестная команда.')
else:
    print("Вы вышли из программы.")
    print(f'Остаток на складе: {storage}')
    print(f'Остаток на магазине 1: {store1}')
    print(f'Остаток на магазине 2: {store2}')
    print(f'Остаток на магазине 3: {store3}')