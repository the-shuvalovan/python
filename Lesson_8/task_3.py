class MyOwnErr(Exception):
    def _init__(self, txt):
        self.txt = txt

result = []
x = 0

while x != "q":
    print("Для выхода их программы - q")
    x = input('Введите число для добавления в список: ')
    try:
        num = int(x)
        result.append(num)
    except (ValueError, MyOwnErr) as err:
        print('Введено не корректное число')
        print(result)
else:
    print("Вы вышли из программы")
    print(result)