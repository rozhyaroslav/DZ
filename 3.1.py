def my_del(arg_1,arg_2):
    if arg_2!= 0:
        return arg_1/arg_2
    else:
        print('Деление на ноль невозможно!')
x1=int(input('Введите частное: '))
x2=int(input('Введите делитель: '))
print(f'Результат: {my_del(x1,x2)}')
