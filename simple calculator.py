def add(x, y):
    return (x + y)

def subtract(x, y):
    return (x - y)

def multiply(x, y):
    return (x * y)

def divide(x, y):
    return (x / y)

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    select = input("Select(1/2/3/4): ")

    # check if choice is one of the four options
    if select in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if select == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif select == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif select == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif select == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
   