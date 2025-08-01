# Task 2: Write and append data to a file

# Step 1: Write to the file
with open("output.txt", "w") as file:
    user_input = input("Enter text to write to the file: ")
    file.write(user_input + "\n")

# Step 2: Append to the same file
with open("output.txt", "a") as file:
    additional_input = input("Enter more text to append to the file: ")
    file.write(additional_input + "\n")

# Step 3: Read and display the final content
print("\n--- Final Content of output.txt ---")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
