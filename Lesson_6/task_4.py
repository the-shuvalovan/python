class Car:
    def __init__(self, speed=0, color='black', name='Сar', is_police=False):
        self.speed = 0
        print(f'Имя автомобиля: {name}, цвет: {color}')

    def go(self, speed=0):
        print(f'Машина едет со скоростью {self.speed} км/ч.')

    def stop(self):
        print('Машина остановилась.')

    def turn(self, direction):
        print(f'Машина повернулась {direction}')

    def show_speed(self, speed=0):
        print(f'Текущая скорость: {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self, **kwargs):
        print(f'Текущая скорость: {self.speed} км/ч')
        if self.speed > 60:
            print('Превышение скорости! Максимально разрашенная скорость - 60 км.ч')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self, **kwargs):
        print(f'Текущая скорость: {self.speed} км/ч')
        if self.speed > 40:
            print('Превышение скорости! Максимально разрашенная скорость - 40 км.ч')

    def turn(self, direction):
        super().turn(direction)


class PoliceCar(Car):
    def __init__(self, speed, name, color='blue'):
        super().__init__(speed, color, name)
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = True


a = TownCar(58, 'red', 'kia')
a.show_speed()
a.go()
a.turn('направо')
a.stop()

b = WorkCar(51, 'white', 'Opel')
b.show_speed()
b.go()
b.turn('налево')
b.stop()

c = PoliceCar(30, 'Ford')
c.show_speed()
c.go()
c.turn('назад')
c.stop()

d = SportCar(150, 'green', 'Ferrari')
d.go()
d.turn('направо')
d.show_speed()
d.stop()
