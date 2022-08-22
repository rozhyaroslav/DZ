sum = 0
vvod = input("Введите числа через пробел: ").split(' ')
with open ("5.5.txt",'w',encoding='utf-8') as f_obj:
    f_obj.write(' '.join(vvod))
    for el in vvod:
        sum+=int(el)
    print(sum)