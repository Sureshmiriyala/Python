class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
            return x / y

calculator = Calculator()


x = int(input("Enter the value1: "))
y = int(input("Enter the value2: "))

print("Addition:", calculator.add(x,y))
print("Subtraction:", calculator.subtract(x,y))
print("Multiplication:", calculator.multiply(x,y))
print("Division:", calculator.divide(x,y))
