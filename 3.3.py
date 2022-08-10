def my_func(x1,x2,x3):
    if x1<x2 and x1<x3:
        return x2+x3
    if x2<x1 and x2<x3:
        return x1+x3
    if x3<x1 and x3<x2:
        return x1+x2
print(my_func (int(input('x1=')), int(input('x2=')),int(input('x3='))))