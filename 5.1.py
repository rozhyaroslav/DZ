with open("5.1.txt", "w") as f_obj:
    vvod=' '
    while vvod!='':
        vvod=input("Введите данные в новую строку:")
        print(vvod, file=f_obj)