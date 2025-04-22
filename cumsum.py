n=int(input("enter a number : "))
s=0
a=[]
# b=[]
for i in range(n):
    a.append(int(input(f'Enter a number {i+1}: ')))

for i in range(n):
    s=s+a[i]
    a[i]=s
print('----------------------------');
print('Cumulative sum of the list is : ',a)
