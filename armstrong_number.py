n=int(input())
p=len(str(n))
s=0
for i in str(n):
    s=s+int(i)**p
if s==n:
    print("Armstrong")
else:
    print("not")

