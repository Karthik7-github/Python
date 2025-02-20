x = input()
y = len(x)
c = 0

for i in range(0,y):
    z = x.count(x[i])
    
    if z==2:
        c=c+1
        print(x[i])
        break


if c==0:
    print("None")  