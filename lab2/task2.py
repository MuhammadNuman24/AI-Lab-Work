
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
    newNum = int(input(f"Enter number {i} for second list: "))
    list2.append(newNum)


# Merge lists
mergeLists = list1 + list2

# Sort the merged list
mergeLists.sort()

# Display result
print("Merged and sorted list:", mergeLists)

newList = len(mergeLists)
print("Length of new list is: ",newList)
smallestNumber=mergeLists[0]
largestNumber=mergeLists[0]
# for small number
for i in range(1,newList):
 if smallestNumber>mergeLists[i]:
    smallestNumber=mergeLists[i]
print("Smallest number is: ",smallestNumber)

# for largest number
for i in range(1,newList):
 if largestNumber<mergeLists[i]:
    largestNumber=mergeLists[i] 
print("Largest number is: ",largestNumber)




