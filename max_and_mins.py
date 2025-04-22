n = int(input('Enter  number of elements to enter : '))
a=[]
for i in range(n):
    a.append(int(input(f'Enter a number {i+1}: ')))
a.sort()
print('----------------------------');
for i in range(n//2):

    print(f'{a[i]} : {a[n-i-1]}')


# print(f"First max : {a[-1]}")
# print(f"Second max : {a[-2]}")
# print(f"Third max : {a[-3]}")
# print(f"First min : {a[0]}")
# print(f"Second min : {a[1]}")
# print(f"Third min : {a[2]}")