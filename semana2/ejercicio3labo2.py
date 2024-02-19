def evaluate_expression(expression, prefix=True):
    character_list = expression.split(" ")

    if prefix:
        character_list.reverse()

    first_number = None
    second_number = None

    for char in character_list:
        if char.isdigit():
            if first_number is None:
                first_number = int(char)
            else:
                second_number = first_number
                first_number = int(char)
        else:
            if char == "+":
                second_number = first_number + second_number
            elif char == "-":
                second_number = second_number - first_number
            elif char == "*":
                second_number = first_number * second_number
            elif char == "/":
                second_number = second_number / first_number
            first_number = None
    print(second_number)

evaluate_expression("+ 1 - 5 * 2 4", True)
evaluate_expression("1 3 + 4 +", False)

