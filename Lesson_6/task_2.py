class Road:
    def __init__(self, length=0, width=0):
        self._length = length
        self._width = width

    def counting(self):
        try:
            if self._length <= 0 or self._width <= 0:
                print('Одна из переменных меньше или равна нулю, расчет не имеет смысла')
            else:
                result = (self._length * self._width * 25 * 5) / 100
                print(f'Для покрытия дороги потребуется {result} тонн асфальта')
        except:
            print('Введены некорректные данные')


a = Road(20, 500)
a.counting()
