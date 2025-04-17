n = int(input("enter a num : "))
num=n
z=n%10
s=0

while n>0:
    n=n//10
    s=s+1 
print(s)
c=0
h=s
while s>0:
    r=num%10
    if r!=z:
        break
    else:
        c=c+1
    num=num//10

    s=s-1

if c==h:
    print("repeating number")
else:
    print("not repeating number")

 


    