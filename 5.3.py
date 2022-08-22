all_zp=0.0
counter_sotr=0
with open("5.3.txt", "w", encoding="utf-8") as f_obj:
    vvod = ' '
    while vvod != '':
        vvod = input("Введите фамилию и зарплату сотрудника через пробел: ")
        if vvod=='': continue
        print(vvod, file=f_obj)

with open("5.3.txt", "r", encoding="utf-8") as f_obj:
    for line in f_obj:
        line=line.rstrip()
        line=list(line.split(' '))
        if float(line[1])<20000:
            print(line[0])
        all_zp+=float(line[1])
        counter_sotr+=1
    print(all_zp/counter_sotr)