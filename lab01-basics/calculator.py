def calculate(left, operator, right):
    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
        return left * right
    if operator == "/":
        if right == 0:
            raise ValueError("Cannot divide by zero.")
        return left / right
    raise ValueError("Choose +, -, * or /.")


if __name__ == "__main__":
    try:
        left = float(input("First number: "))
        operator = input("Operator: ").strip()
        right = float(input("Second number: "))
        print("Result:", calculate(left, operator, right))
    except ValueError as error:
        print(error)
