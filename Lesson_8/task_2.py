class MyOwnErr(Exception):
    def _init__(self, txt):
        self.txt = txt

a = False
b = False

num1 = input('Введите делимое: ')

try:
    a = int(num1)
except (ValueError, MyOwnErr) as err:
    print('Принимается только число!')

num2 = input('Введите делитель: ')

try:
    b = int(num2)
except (ValueError, MyOwnErr) as err:
    print('Принимается только число!')

if a is False or b is False: pass
else:
    try:
        print(a/b)
    except(ZeroDivisionError, MyOwnErr) as err:
        print('Делить на ноль нельзя!')
