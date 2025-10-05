try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("what kind of operation do you want to perform? Press + for addition, - for subtraction, * for multiplication, / for division")
    o = input("Enter operation: ")
    match o:
        case '+':
            print(f"The result of {a} + {b} is {a + b}")
        case '-':
            print(f"The result of {a} - {b} is {a - b}")
        case '*':
            print(f"The result of {a} * {b} is {a * b}")
        case '/':
            if b != 0:
                print(f"The result of {a} / {b} is {a / b}")
            else:
                print("Error: Division by zero is not allowed.")
        case _:
            print("Invalid operation selected. Please choose +, -, *, or /.")

except Exception as e:
    print(f"An error occurred: {e}")