n = int(input('Enter number of elements to enter: '))
a = []

for i in range(n):
    a.append(int(input(f'Enter a number {i+1}: ')))

for i in range(n-1,-1,-1):
    print(a[i],end=' ')