# Get student name
name = input("Enter student's name: ")

# Get marks for 3 subjects
mark1 = float(input("Enter marks for subject 1: "))
mark2 = float(input("Enter marks for subject 2: "))
mark3 = float(input("Enter marks for subject 3: "))

# Calculate average
average = (mark1 + mark2 + mark3) / 3

# Determine grade based on average
if average >= 75:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 40:
    grade = "C"
else:
    grade = "Fail"

# Display results in formatted output
print("\n" + "-" * 30)
print(f"Name     : {name}")
print(f"Average  : {average:.1f}")
print(f"Grade    : {grade}")
print("-" * 30)
