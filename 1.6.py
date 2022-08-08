plus = int(input("Введите сумму выручки фирмы: "));
minus = int(input("Введите сумму издержек фирмы: "));
if plus>minus:
    print("Прибыль!")
    print("Рентабельность: ",(plus-minus)/plus)
    sotrudniki = int(input("Введите количество сотрудников фирмы: "));
    print("Прибыль фирмы на одного сотрудника: ", plus/sotrudniki)
if plus<minus:
    print("Убыток!")