a=list(map(int,input().split()))
n=int(input())
for i in range(n):
    a.insert(0,a.pop())
print(a)