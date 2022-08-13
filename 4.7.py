from math import factorial
n=int(input('Введите число, факториал которого хотите получить: '))
spisok=[]
i=1
while i<=n:
   spisok.append(i)
   i+=1
def fact():
    for el in (spisok):
        yield factorial(el)
result=[el for el in fact()]
print(result)