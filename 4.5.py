from functools import reduce
result=[i for i in range(1001) if (100<=i<=1000) and i%2==0]
def my_func(a, b) : return a * b
print(reduce(my_func, result))