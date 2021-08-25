class Calculator:

    def __init__(self, num):
        self.num = num

    def __add__(self, a):
        return self.num+a

    def __sub__(self, a):
        return self.num-a

    def __mul__(self, a):
        return self.num*a

    def __truediv__(self, a):
        return self.num/a


x, y = input("Enter num1 num2 : ").split(",")

x = Calculator(int(x))
y = int(y)
print(x+y, x-y, x*y, x/y, sep="\n")
