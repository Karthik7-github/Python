x = list(map(int,input().split()))
y = list(map(str,input().split()))
c=0
dict = {}
for i in x:
    dict[i] = y[c]
    c=c+1
print(dict)

