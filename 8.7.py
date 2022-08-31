class ComplexNumber:
    def __init__(self, a1, a2, *args):
        self.a1 = a1
        self.a2 = a2
        self.result = 'a1 + a2 * i'
    def __add__(self, other):
        print(f'Сумма compl1 и compl2 равна')
        return f'result = {self.a1 + other.a1} + {self.a2 + other.a2} * i'
    def __mul__(self, other):
        print(f'Произведение compl1 и compl2 равно')
        return f'result = {self.a1 * other.a1 - (self.a2 * other.a2)} + {self.a2 * other.a1} * i'
    def __str__(self):
        return f'result = {self.a1} + {self.a2} * i'

compl_1 = ComplexNumber(4, -4)
compl_2 = ComplexNumber(2, 8)
print(compl_1)
print(compl_1 + compl_2)
print(compl_1 * compl_2)