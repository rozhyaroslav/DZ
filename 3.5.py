#Я понимаю, что урок по функциям, но в задании условия наличия функции я не нашел
#Поэтому описал алгоритм, который пришел в голову в первую очередь)
#По сути, функцией можно было заменить строки с 7 по 11 и с 15 по 18
# А бинарную переменную так и так я бы использовал для проверки соблюдения условия ввода "!"
sum=0
stop_sign=False
while stop_sign==False:
    numbers=input("Введите числа через пробел (стоп символ '!'): ")
    numbers=list(numbers.split(' '))
    sum_new=0
    i=0
    while i<len(numbers) and stop_sign==False:
        if numbers[i]=="!":
            stop_sign=True
            continue
        sum_new = sum_new + int(numbers[i])
        i+=1
    sum+=sum_new
    print(sum)