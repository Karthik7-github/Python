f = open("cube.txt","w")
data = list(map(int,input().split()))
lis=[]
for i in data:
    lis.append(str(i**3)+'\n')

f.writelines(lis)
f.close()
