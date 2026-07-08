try:
    # Taking user input
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    # Display result
    print("Result:", result)

# Handles invalid input (e.g., string instead of integer)
except ValueError:
    print("Error: Please enter valid integers.")

# Handles division by zero
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# Handles any other unexpected exception
except Exception as e:
    print("Unexpected error occurred:", e)

# This block always executes
finally:
    print("Program execution completed.")
