class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def substraction(self):
        return self.a - self.b


mathObj = Math(6, 2)
print(mathObj.division())
print(mathObj.multiplication())
print(mathObj.addition())
print(mathObj.substraction())
