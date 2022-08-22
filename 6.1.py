from time import sleep
from datetime import datetime

class TrafficLight:
    _COLORS = {'красный': int(input("Введите длительность красного сигнала \n (по условию '7'): ")),
               'жёлтый': int(input("Введите длительность желтого сигнала \n (по условию '2'): ")),
               'зеленый': int(input("Введите длительность зеленого сигнала \n (по условию 'любое значение'): "))}
    _color = None
    def running(self):
        for COLOR, time_change in self._COLORS.items():
            self._color = COLOR
            start_time = datetime.now()
            print("Выполнение:")
            print(f"На светофоре горит {self._color} на протяжении {time_change} секунд")
            if (time_change != 7 and COLOR=='красный') or (time_change != 2 and COLOR=='жёлтый'):
                print("Ошибка!!")
                break
            sleep(time_change)
            print("Проверка:")
            print(f"На светофоре горел {self._color} на протяжении {(datetime.now() - start_time).seconds} секунд")
        sleep(time_change)
result = TrafficLight()
result.running()
