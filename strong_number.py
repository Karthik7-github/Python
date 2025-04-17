n=int(input("Enter a number : "))
num=n
def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)

s=0
while(n>0):
    rem=n%10
    s=s+fact(rem)
    n=n//10

if(num==s):
    print("Strong number ")
else:
    print("Not a strong number ")

