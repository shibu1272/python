# Task 1: Perform Basic Mathematical Operations

# Step 1: Take two numbers as input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Step 2: Perform basic mathematical operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Step 3: Handle division carefully to avoid ZeroDivisionError
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (cannot divide by zero)"

# Step 4: Display the results
print("\n--- Results ---")
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")
