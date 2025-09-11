
list1 = []

fistlength=input("Enter length of first list: ")
fistlength=int(fistlength)
for i in range(1,fistlength+1):
    num = int(input(f"Enter number {i} for first list: "))
    list1.append(num)

list2 = []
secondlength=input("Enter length of second list: ")
secondlength=int(secondlength)
for i in range(1,secondlength+1):
    num = int(input(f"Enter number {i} for second list: "))
    list2.append(num)


# Merge lists
mergeLists = list1 + list2

# Sorting the final list
mergeLists.sort()

print("Merged and sorted list:", mergeLists)
