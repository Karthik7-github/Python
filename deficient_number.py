n=int(input("Enter a number : "))
a=[]
for i in range(1,n,1):
    if n%i==0:
        a.append(i)
s=0
for i in a:
    s=s+i
if s<n:
    print("Deficient number")
else:
    print("not a Deficient number")