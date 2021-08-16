import time


def out_red(text):
    print("\033[31m {}".format(text))


def out_yellow(text):
    print("\033[33m {}".format(text))


def out_green(text):
    print("\033[32m {}".format(text))


class TrafficLight:
    __color = 'red'

    def running(self):
        __color = 'red'
        out_red(f"Загорелся красный свет – \n Нам вперед дороги нет. \n")
        time.sleep(7)
        __color = 'yellow'
        out_yellow(f'Желтый свет – предупрежденье: \n Жди сигнала для движенья. \n')
        time.sleep(2)
        __color = 'green'
        out_green(f'Свет зеленый говорит: \n «Проходите, путь открыт!» \n')
        time.sleep(10)
        __color = 'red'
        out_red(f"Загорелся красный свет – \n Нам вперед дороги нет. \n")


a = TrafficLight()
a.running()
