name=list(input('Введите название товаров через пробел: ').split(' '))
price=list(input('Введите стоимость товаров через пробел: ').split(' '))
kolvo=list(input('Введите количество товаров через пробел: ').split(' '))
ed_izm=list(input('Введите единицы измерения товаров через пробел: ').split(' '))
k=0
data_base=list('')
while k<len(name):
    dict={'название':name[k],'цена':price[k], 'количество':kolvo[k], 'ед':ed_izm[k]}
    kortage= (k+1, dict)
    data_base.append(kortage)
    k+=1
print(data_base)
key_word=str(input('Введите ключ-характеристику: '))
analytic_dict={'название':name, 'цена':price, 'количество':price, 'ед':ed_izm}
print(analytic_dict.get(key_word))