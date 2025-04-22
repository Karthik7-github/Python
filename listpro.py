n = int(input("Enter no of numbers we have to enter : "))
l=[]
for i in range(n):
    l.append(int(input("Enter the number : ")))
l.sort()
print("The sorted list is : ",l)
print("The 2nd largest number is : ",l[-2])
print("even numbers are : ")
for i in range(n):
    if l[i]%2==0:
        print(l[i])

print("odd numbers are : ")   
for i in range(n):
    if l[i]%2==1:
        print(l[i])




