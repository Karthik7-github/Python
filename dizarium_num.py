n=int(input())
p=1
s=0
for i in str(n):
    s=s+int(i)**p
    p=p+1
if s==n:
    print("Dizarium")
else:
    print("not")