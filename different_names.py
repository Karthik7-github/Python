x = input() #raghu
y = input() #raghuvaran

a = len(x)
b = len(y)

if a>b:
    for i in range(b):
        if x[i]!=y[i]:
            c = i+1
            break
else:
    for i in range(a):
        if x[i]!=y[i]:
            c = i+1
            break 

print(c)