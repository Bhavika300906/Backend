try:
    # Take input from user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter operator (+, -, *, /): ")

    # Perform operation
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2   # May raise ZeroDivisionError
    else:
        print("Invalid operator!")
        result = None

    # Display result
    if result is not None:
        print("Result:", result)

# Handle division by zero
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# Handle invalid input (like string instead of number)
except ValueError:
    print("Error: Invalid input! Please enter numeric values.")

# Handle any other unexpected errors
except Exception as e:
    print("Unexpected error:", e)
