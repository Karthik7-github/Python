n=input().split()
for i in range(len(n)):
    if i==0:
        n[i]=n[i].lower()
    else:
        n[i]=n[i].capitalize()

print("".join(n))
