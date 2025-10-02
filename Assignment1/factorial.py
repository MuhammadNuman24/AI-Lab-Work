print("Enter the number to find factorial : ")
number=input()
number=int(number)
fact=1
negative=0
if number > 1:
 while number > 1:
  fact=fact*number
  number=number-1
 print("Factorial of the number is : " , fact)
elif number == 0 or number==1:
 print("Factorial of the number is : 1")
else:
  print("Invalid input")