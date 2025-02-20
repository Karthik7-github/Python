# programming
# #
# 3
# pr#gr#mm#ng

x = input()
y = input()

z = int(input())

a = []
if z >len(x):
        print("invalid")
else:
    for i in range(0,len(x)):
         if (i+1)%z==0:
           a.append(y)    
         else:
            a.append(x[i])

b =''.join(str(k) for k in a )
print(b)              