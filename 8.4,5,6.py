class Sklad_org_tech:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_position = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def priemka(self):
        try:
            position = input(f'Введите наименование ')
            position_price = int(input(f'Введите цену за ед '))
            position_quantity = int(input(f'Введите количество '))
            full_info = {'Модель устройства': position, 'Цена за ед': position_price, 'Количество': position_quantity}
            self.my_position.update(full_info)
            self.my_store.append(self.my_position)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад - {self.my_store_full}')
            return f'Выход'
        else:
            return Sklad_org_tech.priemka(self)


class Printer(Sklad_org_tech):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(Sklad_org_tech):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Copier(Sklad_org_tech):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'


position_1 = Printer('HP', 2000, 5, 10)
position_2 = Scanner('Samsung', 1200, 5, 10)
position_3 = Copier('Xerox', 1500, 1, 15)
print(position_1.priemka())
print(position_2.priemka())
print(position_3.priemka())
print(position_1.to_print())
print(position_3.to_copier())