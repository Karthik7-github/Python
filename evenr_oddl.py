n=int(input("enter the number of elements : "))
a=[]
for i in range(n):
    a.append(int(input("enter the number : ")))

for i in a:
    if i%2==0:
        a.append(i)
for i in a:
    if i%2==1:
        a.append(i)
for i in range(0,n,1):
    a.remove(a[i])

print(a)

