i=1
class Error:
    def __init__(self,a):
        self.my_list = []
    def add_elements(self):

        while i>0:
            try:
                val1 = float(input('Введите значения и нажимайте Enter - '))
                self.my_list.append(val1)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение - строка и булево")
                alternative = input(f'Попробовать еще раз? +/- ')

                if alternative == '+':
                    print(try_except.add_elements())
                elif alternative == '-':
                    return f'Всего хорошего!'
                else:
                    return f'До свидания!'

try_except = Error(1)
print(try_except.add_elements())