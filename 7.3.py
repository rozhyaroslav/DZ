class Cell:
    def __init__(self, kolvo):
        self.kolvo = int(kolvo)
    def __str__(self):
        return f'Результат операции {self.kolvo * "*"}'
    def __add__(self, other):
        return Cell(self.kolvo + other.kolvo)
    def __sub__(self, other):
        if self.kolvo - other.kolvo > 0:
            return self.kolvo - other.kolvo
        else: print('Количество клеток меньше нуля!')
    def __mul__(self, other):
        return Cell(int(self.kolvo * other.kolvo))
    def __truediv__(self, other):
        return Cell(round(self.kolvo // other.kolvo))
    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.kolvo / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.kolvo % cells_in_row)}'
        return row
cell_A = Cell(34)
cell_B = Cell(18)
print(cell_A)
print(cell_B)
print(cell_A + cell_B)
print(cell_A - cell_B)
print(cell_A.make_order(6))
print(cell_B.make_order(9))
print(cell_A / cell_B)