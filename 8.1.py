class Date:
    def __init__(self, dd_mm_yyyy):
        self.dd_mm_yyyy = str(dd_mm_yyyy)

    @classmethod
    def splitter(cls, dd_mm_yyyy):
        my_date=dd_mm_yyyy.split('-')
        return int(my_date[0]),int(my_date[1]),int(my_date[2])

    @staticmethod
    def check_up(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 0:
                    return f'Дата введена правильно!'
                else:
                    return f'Ошибка при вводе года!'
            else:
                return f'Ошибка при вводе месяца!'
        else:
            return f'Ошибка при вводе дня!'

    def __str__(self):
        return f'Текущая дата {Date.splitter(self.dd_mm_yyyy)}'

today = Date('27 - 8 - 2022')
print(today)
print(Date.check_up(2, 3, 201))
print(today.check_up(11, 13, 2011))
print(Date.splitter('27 - 1 - 2011'))
print(today.splitter('11 - 11 - 2020'))