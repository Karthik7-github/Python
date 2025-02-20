# m=int(input())
# d=int(input())
# x=m
# while(d>1):
#     if x==m:
#         continue
#     else:
#         m=m+200
#         d=d-1
# print(m)

a=int(input())
s=0
while(a>0):
    rem = a%10
    if rem%2!=0:
        s=s+rem
    a=int(a/10)
print(s)