class ZeroDevision:
    def __init__(self, numerator, quotient):
        self.numerator = numerator
        self.quotient = quotient

    @staticmethod
    def divide_by_zero(numerator, quotient):
        try:
            return (numerator / quotient)
        except:
            return (f"Деление на ноль недопустимо!")

div = ZeroDevision(10,0)
print(ZeroDevision.divide_by_zero(int(input("Введите числитель:")), int(input("Введите знаменатель:"))))