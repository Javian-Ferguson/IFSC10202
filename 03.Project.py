# Simple Calculator Program

# Prompt for first number
num1 = float(input("Enter First Number: "))

# Prompt for operator
operator = input("Enter Operator (+,-,*,/): ")

# Prompt for second number
num2 = float(input("Enter Second Number: "))

# Perform calculation based on operator
if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero")
else:
    print("Invalid Operator")
