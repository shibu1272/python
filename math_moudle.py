import math

# Step 1: Ask the user for a number
num = float(input("Enter a positive number: "))

# Step 2: Perform calculations using math module
if num > 0:
    sqrt_val = math.sqrt(num)
    log_val = math.log(num)          # Natural logarithm (base e)
    sine_val = math.sin(num)         # Sine (expects radians)

    # Step 3: Display results
    print("\n--- Results ---")
    print(f"Square root of {num} = {sqrt_val}")
    print(f"Natural logarithm (ln) of {num} = {log_val}")
    print(f"Sine of {num} radians = {sine_val}")
else:
    print("Please enter a number greater than 0 for valid calculations.")
