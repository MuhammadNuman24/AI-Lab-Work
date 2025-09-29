name=input("Enter your name: ")
roll_number=input("Enter your roll number: ")
cgpa=input("Enter your CGPA: ") 
semester=input("Enter your current semester: ")
program=input("Enter your program: ")   
university=input("Enter your university: ")


with open("my-details.txt", "w") as file:
    file.write("Roll Number: " + roll_number +  "\n")
    file.write("Name: " + name +  "\n")
    file.write("CGPA: " + cgpa +  "\n")
    file.write("Current Semester:" + semester +  "\n")
    file.write("Program: " + program +  "\n")
    file.write("University:" + university +  "\n")

print("✅ File 'my-details.txt' has been created and details written successfully!")
