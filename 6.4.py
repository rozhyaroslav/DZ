class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed=speed
        self.color=color
        self.name=name
        self.is_police=is_police
    def go(self):
        return f'{self.name} поехала!'
    def stop(self):
        return f'{self.name} остановилась!'
    def turn(self, direction):
        return f'{self.name} повернула {direction}!'
    def show_speed(self):
        return f'Текущая скорость {self.name} - {self.speed}км/ч'
class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"Превышение скорости на {self.speed-60}!!!"
        else: return f'Текущая скорость {self.name} - {self.speed}км/ч'
class SportCar(Car):
    None
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"Превышение скорости на {self.speed-40}!!!"
        else: return f'Текущая скорость {self.name} - {self.speed}км/ч'
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        self.speed=speed
        self.color=color
        self.name=name
        self.is_police=is_police
Ferrari = SportCar(150,'yellow','Ferrari')
print(Ferrari.go())
print(Ferrari.is_police)
print(Ferrari.turn('налево'))
print(Ferrari.show_speed())
print(Ferrari.stop())
UAZ = PoliceCar(80, 'white', 'UAZ_Hunter')
print(UAZ.go())
print(UAZ.is_police)
print(UAZ.turn('назад'))
print(UAZ.show_speed())
print(UAZ.stop())
Renault = WorkCar(60, 'blue', 'Renault Logan')
print(Renault.go())
print(Renault.is_police)
print(Renault.turn('на 45 градусов'))
print(Renault.show_speed())
print(Renault.stop())
Mitsubishi = TownCar(60, 'blue', 'Mitsubishi Galant')
print(Mitsubishi.go())
print(Mitsubishi.is_police)
print(Mitsubishi.turn('направо'))
print(Mitsubishi.show_speed())
print(Mitsubishi.stop())