class Textil:
    def __init__(self,name, V, H):
        self.name=name
        self.V = V
        self.H = H

    def square_of_coat(self):
        return self.V / 6.5 + 0.5

    def square_of_jacket(self):
        return self.H * 2 + 0.3

    @property
    def full_square(self):
        return str(f'Общая площадь ткани для пошива вещей {round(coat.square_of_coat() + jacket.square_of_jacket(),1)}')


class Coat(Textil):
    def __init__(self, name,V, H):
        super().__init__(name, V, H)
        self.sq_coat = round((self.V / 6.5 + 0.5),2)
    def __str__(self):
        return f'Площадь на пальто фирмы {self.name}: {self.sq_coat}'

class Jacket(Textil):
    def __init__(self, name, V, H):
        super().__init__(name, V, H)
        self.sq_jacket = (self.H * 2 + 0.3)
    def __str__(self):
        return f'Площадь на костюм фирмы {self.name}: {self.sq_jacket}'

coat = Coat('Adidas',2, 4)
jacket = Jacket('Nike',1, 2)
print(coat)
print(jacket)
print(coat.full_square)
print(f'Площадь ткани на пошив пальто фирмы {coat.name} {round(coat.square_of_coat(),1)}')
print(f'Площадь ткани на пошив куртки фирмы {jacket.name} {round(jacket.square_of_jacket(),1)}')