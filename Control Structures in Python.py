# Task 1: Check if a Number is Even or Odd

# Step 1: Take integer input from the user
num = int(input("Enter an integer: "))

# Step 2: Use if-else to check even or odd
if num % 2 == 0:
    print(f"{num} is Even.")
else:
    print(f"{num} is Odd.")



# Task 2: Sum of Integers from 1 to 50 Using a Loop

# Initialize sum variable
total_sum = 0

# Use for loop to add numbers from 1 to 50
for i in range(1, 51):
    total_sum += i

# Display the final sum
print(f"The sum of integers from 1 to 50 is: {total_sum}")
