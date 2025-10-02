# 1.Write a program that keeps reading integers until 
# the user enters 0, then prints the sum of all  entered values.

total = 0

while True:
    num = (input("Enter any Number to find Sum or enter 0 to stop : "))
    num = int(num)
    if num == 0:
     break
    else:
     total = total+ num

print("The sum of all entered values is:", total)
