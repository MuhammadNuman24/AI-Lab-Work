
even_sum = 0
odd_sum = 0

for i in range(1, 10):
    num = int(input(f"Enter integer {i}: "))
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

# Print results
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
