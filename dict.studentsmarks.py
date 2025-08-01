# Task 1: Dictionary of Student Marks

# Step 1: Create the dictionary
student_marks = {
    "Aadhya": 89,
    "Krisha": 95,
    "Vedant": 78,
    "Parshv": 88,
    "Mittal": 91
}

# Step 2: Ask user to input a student's name
name = input("Enter the student's name: ")

# Step 3: Retrieve and display the marks
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print(f"Student '{name}' not found in the record.")
