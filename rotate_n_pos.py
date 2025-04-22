n = int(input('Enter number of elements to enter: '))
a = []

for i in range(n):
    a.append(int(input(f'Enter a number {i+1}: ')))

z = int(input("No of positions to rotate: "))


z = z % n  
a = a[z:] + a[:z]  

print('----------------------------')
print('List after rotating is:', a)
