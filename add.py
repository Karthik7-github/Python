o = []
e = []

n = int(input())

for i in range(0,n):
    x = int(input("enter : "))
    if x%2==0:
           e.append(x)
    else :
        o.append(x)


print(o)
print(e)