class Date:

    def __init__(self, date):
        self.date = date

    @classmethod
    def __adapt__(cls, param):
        day, month, year = param.split('-')
        print(day, month, year)
        return day, month, year

    @staticmethod
    def __validate__(obj):
        day, month, year = obj.date.split('-')

        try:
            d = int(day)
            m = int(month)
            y = int(year)
            if m < 1 or m > 12:
                print('Указан не правильный месяц')
            elif d < 1 or d > 31:
                print('Указан не правильный день')
            elif m == 2 and y % 4 == 0 and d > 29:
                print('Указан не правильный день, в этом месяце 29 дней')
            elif m == 2 and y % 4 != 0 and d > 28:
                print('Указан не правильный день, в этом месяце 28 дней')
            elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
                if d < 1 or d > 31:
                    print('Указан не правильный день')
                else:
                    print(f'Дата {obj.date} валидна.')
            elif m == 2 or m == 4 or m == 6 or m == 9 or m == 11:
                if d < 1 or d > 30:
                    print('Указан не правильный день')
                else:
                    print(f'Дата {obj.date} валидна.')
            else:
                print(f'Дата {obj.date} валидна.')

        except:
            print('Введен не правильный формат данных')


Date.__adapt__('03-09-2021')
a = Date('24-08-2021')
Date.__validate__(a)
