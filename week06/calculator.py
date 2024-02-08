class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x + y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Cannot divide by zero"
        return x / y

    def modulo(self, x, y):
        return x % y

    def power(self, x, y):
        return x ** y

    def square_root(self, x):
        return x ** (1 / 2)


def main():
    calc = Calculator()

    operation = input("Enter operation (add, subtract, multiply, divide, modulo, power, square_root): ")

    if operation == "square_root":
        x = float(input("Enter number: "))
        print(calc.square_root(x))
    elif operation in ["add", "subtract", "multiply", "divide", "modulo", "power"]:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        if operation == "add":
            print(calc.add(x, y))
        elif operation == "subtract":
            print(calc.subtract(x, y))
        elif operation == "multiply":
            print(calc.multiply(x, y))
        elif operation == "divide":
            print(calc.divide(x, y))
        elif operation == "modulo":
            print(calc.modulo(x, y))
        elif operation == "power":
            print(calc.power(x, y))
    else:
        print("Invalid operation")


if __name__ == "__main__":
    main()

