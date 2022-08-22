from time import sleep
from datetime import datetime
class TrafficLight:
    _COLORS = {'красный': 7, 'жёлтый': 2, 'зеленый': 10}
    _color = None
    def running(self):
        for COLOR, time_change in self._COLORS.items():
            self._color = COLOR
            start_time = datetime.now()
            print("Выполнение:")
            print(f"На светофоре горит {self._color} на протяжении {time_change} секунд")
            sleep(time_change)
            print("Проверка:")
            print(f"На светофоре горел {self._color} на протяжении {(datetime.now() - start_time).seconds} секунд")
        sleep(time_change)
result = TrafficLight()
result.running()
