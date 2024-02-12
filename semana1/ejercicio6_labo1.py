x = float(input("Enter a number: "))
y = float(input("Enter another number: "))
c = input("Enter an operation (+, -, *, /, ^): ")


def calculator(operator, a, b):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    elif operator == "^":
        return a ** b
    else:
        return "Invalid operation"


print(calculator(c, x, y))
