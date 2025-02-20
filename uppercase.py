x = input().strip()
c=0
for i in x:
    if int(i)<=65 and int(i)>=90:
        c=c+1

print(c)