mylist1=[]
print("enter objects of first list: ")
for i in range(5):
 val=input("enter a value: ")
 n=int(val)
 mylist1.append(n)
mylist2=[]
print("enter objects of 2nd list")
for i in range(5):
 val=input("enter a value:")
 n=int(val)
 mylist2.append(n)
list3=mylist1+mylist2
print(list3)