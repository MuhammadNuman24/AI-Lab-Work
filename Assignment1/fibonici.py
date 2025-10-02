# Program to display the first N Fibonacci numbers

num = (input("Enter how many Fibonacci numbers you want: "))
num=   int (num)
a, b = 0, 1
count = 0

print("Fibonacci sequence:")

while count < num:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
