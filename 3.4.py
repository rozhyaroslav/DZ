def my_func(x,y):
    i=1
    res=1
    print(x**y)
    while i<=abs(y):
        res=res*(1/x)
        i+=1
    print(res)
print(my_func(int(input('Введите x: ')), int(input('Введите y: '))))