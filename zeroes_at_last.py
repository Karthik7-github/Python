n=int(input("enter a number : "))
a=[]
for i in range(n):
    a.append(int(input(f'Enter a number {i+1}: ')))

for i in range(0,n,1):
    if a[i]==0:
        a.pop(i)
        a.append(0)

print(a)