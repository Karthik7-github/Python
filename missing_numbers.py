n=int(input("enter a number : "))
a=[]
for i in range(n):
    a.append(int(input(f'Enter a number {i+1}: ')))

b=[]
for i in range(1,max(a)):
    if i not in a:
        b.append(i) 
           

for i in b:
      print(i,end=' ')


