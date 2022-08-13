spisok=list(input('Введите числа через пробел: ').split(' '))
result=[spisok[i] for i in range(len(spisok)-1) if int(spisok[i-1])<int(spisok[i]) and i!=0]
print(result)