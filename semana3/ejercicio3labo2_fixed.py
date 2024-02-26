operators = ["+", "-", "*", "/"]

def calculate(operator, first, second):
    if operator == "+":
        return first + second
    elif operator == "-":
        return first - second
    elif operator == "*":
        return first * second
    elif operator == "/":
        return first / second

def evaluate(expr: list):
    token = expr.pop(0)

    if token in operators:
        return calculate(token, evaluate(expr), evaluate(expr))
    else:
        return int(token)

expressions = ["+ 1 - 5 * 2 4", "+ + 3 4 * 2 5", "1 3 + 4 +"]

for expression in expressions:
    x = expression.split(" ")
    if expression[0] not in operators:
        x.reverse()
    result = evaluate(x)
    print(result)
