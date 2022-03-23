class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        return '*' * self.cell

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        return self.cell - other.cell

    def __mul__(self, other):
        return self.cell * other.cell

    def __truediv__(self, other):
        return self.cell // other.cell

    def make_order(self, row):
        self.row = row
        n = self.cell // self.row
        k = self.cell % self.row
        for i in range(n):
            print('*' * row)
        print('*' * k)


a = Cell(14)
print(a)
a.make_order(3)

b = Cell(9)
b.make_order(2)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
