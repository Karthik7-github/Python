n=int(input("enter a number : "))
num=n
s=0
while n>0:
    n=n//20
    s=s+1
print(s)
k=0
while(s>0):
    rem=num%10
    k=k+rem*10
    num=num//10


