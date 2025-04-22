n = int(input('Enter  number of elements to enter : '))
a=[]
for i in range(n):
    a.append(int(input(f'Enter a number {i+1}: ')))

b=[]
for i in a:
    if i not in b:
        b.append(i)

    

print('----------------------------');
print('List after removing duplicates is : ',b)