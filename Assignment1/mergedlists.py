list1 = list(map(int, input("Enter elements of first list separated by space: ").split()))
list2 = list(map(int, input("Enter elements of second list separated by space: ").split()))

# Merge lists
merged = list1 + list2

n = len(merged)
for i in range(n):
    for j in range(0, n - i - 1):
        if merged[j] > merged[j + 1]:
            # swap
            temp = merged[j]
            merged[j] = merged[j + 1]
            merged[j + 1] = temp     

print("Merged sorted list :", merged)
