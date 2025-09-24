def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

while True:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    op = input("Enter operator (+, -, *, /) or 'q' to quit: ")

    if op == "q":
        print("Exiting calculator...")
        break
    elif op == "+":
        print("Result:", add(a, b))
    elif op == "-":
        print("Result:", sub(a, b))
    elif op == "*":
        print("Result:", mul(a, b))
    elif op == "/":
        print("Result:", div(a, b))
    else:
        print("Invalid operator!")

    print("-" * 50)
