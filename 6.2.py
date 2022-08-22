class Road:
    length=20
    width = 5000
    def __init__(self,mass=int(input("Введите массу: ")),fatness=int(input("Введите толщину:"))):
        self._length=Road.length
        self._width=Road.width
        self._mass=mass
        self._fatness=fatness
    def result(self):
        self.full_mass=self._length*self._width*self._mass*(self._fatness*0.001)
        print(f'Масса дорожного полотна составит: {int(self.full_mass)} т.')
a=Road()
a.result()