from itertools import count, cycle
number_of_iterator=input('Укажите интересующий Вас итератор (1 или 2): ')
# Первый итератор:
if number_of_iterator == '1':
    begin=int(input('Укажите число, с которого начнет итератор: '))
    end=int(input('Укажите число, на котором итератор остановится: '))
    for el in count(begin):
        if el > end:
            break
        else:
            print(el)
# Второй итератор:
if number_of_iterator == '2':
    spisok = list(input('Введите числа через пробел: ').split(' '))
    number_repeat=int(input('Укажите сколько раз повторить строку: '))*len(spisok)
    counter = 0
    for el in cycle(spisok):
        if counter > number_repeat-1:
            break
        print(el)
        counter += 1