stroka = input('Введите несколько слов через пробел: ');
stroka_v_liste=stroka.split(' ');
i=0;
counter_strok=1;
while i<len(stroka_v_liste):
    if len(stroka_v_liste[i])>=10:
        print(f"{counter_strok}) {stroka_v_liste[i][0:10]}")
        i+=1
        counter_strok+=1
        continue;
    else:
        print(f"{counter_strok}) {stroka_v_liste[i]}")
        counter_strok+=1
        i+=1