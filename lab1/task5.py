
marks = int(input("Enter marks (1-100): "))

# Check marks range
if marks < 1 or marks > 100:
    print("Invalid marks! Please enter between 1 and 100.")
else:
    if marks < 50:
        grade = "F"
    elif marks <= 60:
        grade = "E"
    elif marks <= 70:
        grade = "D"
    elif marks <= 80:
        grade = "C"
    elif marks <= 90:
        grade = "B"
    else:  # 91 to 100
        grade = "A"

    print(f"Your Marks are :{marks} and Grade is :{grade} ")
