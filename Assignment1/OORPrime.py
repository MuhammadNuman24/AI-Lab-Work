# Program to check even/odd and prime number

num = (input("Enter an integer: "))
num = int(num)
# Check even or odd
if num % 2 == 0:
    print(num, "is Even Number")
else:
    print(num, "is Odd Number")

# Check prime
if num <= 1:  # If number is 1 or less than 1, it's not prime
 print(num , " is NOT a prime number ❌")
else:
 for i in range(2, num):
        if num % i == 0:   # If divisible, it's not prime
           print(num , " is NOT a prime number ❌")
           break
        else:
            print(num , " is a PRIME number ✅")
            break