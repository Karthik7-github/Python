n=int(input("enter a number : "))
num=n
s=0
while n>0:
    rem=n%10
    s=s+rem
    n=n//10

if num%12==0:
    print("Hazard number ")
else:
    print("Not a Hazard number ")
    