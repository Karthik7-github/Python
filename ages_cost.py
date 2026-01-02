a=list(map(int,input().split()))
s=0
if len(a)<31:
    for i in a:
        if i>0 and i<120:
            if i>0 and i<13:
                s=s+350
            elif i>13 and i<60:
                s=s+450
            else:
                s=s+300
print(s)