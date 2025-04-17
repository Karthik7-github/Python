n=int(input("enter no of numbers u want : "))
a=2
b=1
while(n>0):
    z=a
    a=b
    b=z+b
    print(z)
    n=n-1
