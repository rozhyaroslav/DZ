spisok=list(input('Введите числа через пробел: ').split(' '))
result=[el for el in spisok if spisok.count(el)<2]
print(result)