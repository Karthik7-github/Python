x = input()
y = input()
c=0
if x==y:
    print("both are same")
else:
    z = abs(len(x)-len(y))
    for i in x:
        for j in y:
           if i==j:
             c=c+1
        else:
           print(f"first differ at {c} position")
