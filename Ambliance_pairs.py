a=int(input("enter a : ")) #220
b=int(input("enter b : ")) #284
c=[]
s=0
for i in range(1,b,1):
    if(b%i==0):
        c.append(i)
    for i in c :
        s=s+i
if(s==a):
    print("perfect pair")
else:
    print("not a perfect pair")
