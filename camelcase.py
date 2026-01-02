s=input().split(" ")
a=[]
for i in s:
    a.append(i[0].swapcase()+i[1:].lower())
print(" ".join(a))