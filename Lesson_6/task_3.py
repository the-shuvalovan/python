class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        _income = {"wage": 10000, "bonus": 5000}


class Position(Worker):
    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)
        self._income = {"wage": 10000, "bonus": 5000}

    def get_full_name(self):
        return (str(self.name + " " + self.surname))

    def get_full_income(self):
        return (a := (sum(self._income.values())))


r = Position("Вася", "Пупкин", 'специалист')
print(r.get_full_name())
print(r.get_full_income())
