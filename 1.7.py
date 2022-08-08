a=int(input("Введите результат спортсмена в первый день: "));
b=int(input("Введите нужный прирост результата: "));
a1=a;
promezh_rez=0;
i=1
while i < 1000:
    print (i,"-й день: ", a1)
    promezh_rez = a1 * 1.1;
    i = i + 1;
    a1 = promezh_rez;
    if promezh_rez > b:
        print (i,"-й день: ", a1)
        print("Ответ: на ",i,"-й день спортсмен достиг результата — не менее",b," км.")
        break