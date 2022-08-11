listok=list(input('Введите слова через пробел: ').split((' ')))
print(listok)
result=[]
def int_func(arg_1):
    return arg_1.title()
i=0
while i<len(listok):
    result.append(int_func(listok[i]))
    i+=1
print(result)

