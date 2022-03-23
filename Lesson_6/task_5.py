class Stationery:
    title = 'Stationery'

    def draw():
        print('Запуск отрисовки')


class Pen(Stationery):

    def draw():
        print('Запуск отрисовки ручкой')


class Pencil(Stationery):

    def draw():
        print('Запуск отрисовки карандашом')


class Handle(Stationery):

    def draw():
        print('Запуск отрисовки маркером')


a = Pen
a.draw()
b = Pencil
b.draw()
c = Handle
c.draw()
