n = int(input("Enter the number of days : "))
a=[]
for i in range(1,n+1,1):
    a.append(int(input("enter the profit for day "+str(i)+" : ")))
        
k=a[1]
b=[]
for i in a:
    b.append(i)
 
print(f'the profit is {b[-1]-k}')

