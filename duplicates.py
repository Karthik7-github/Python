print("enter the ele :")
a = list(map(int,input().split()))
b = []
c= 0
for i in a:
    x = a.count(i)
    if(x>1):
        if i not in b:
         b.append(i)

print("the duplicates are : ")
print(b)