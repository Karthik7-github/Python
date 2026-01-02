a=list(map(int,input().split()))
c=0
for i in range(len(a)//2):
    if a[i]!=a[-i-1]:
        print("NOT")
        c=1
        break
if c==0:
    print("YES")
