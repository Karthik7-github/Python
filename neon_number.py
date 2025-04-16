n = int(input("enter a number : "))
s=0
k=n*n
while k>0:
    rem=k%10
    s=s+rem
    k=k//10

if n==s:
    print("NEON num")
else:
    print("Not a NEON ")