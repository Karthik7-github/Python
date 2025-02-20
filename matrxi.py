x = int(input())
y = x
a = [[0 for _ in range(y)] for _ in range(x)]

for i in range(x):
    for j in range(y):
        a[i][j] = int(input())

sum = a[0][0] + a[0][y-1] + a[x-1][0] + a[x-1][y-1]      
print(sum)