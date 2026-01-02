num = int(input())
m=num%10
while(num>0):
    r=num%10
    m=min(r,m)
    num//=10
print(m)