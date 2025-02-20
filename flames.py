x = input("Enter first Name  : ")
y = input("Enter second Name : ")
d = []
for i in x :
    for j in y:
        if i==j:
           if i not in d:
              d.append(i)

# print(d)
a = len(x)
b = len(y)
c = (a+b) - 2*len(d)
print(c)

e = "flames"
z = list(e)
while len(z)>1:
    index = (c % len(z)) - 1  
    if index >= 0:
        z = z[index + 1:] + z[:index] 
    else:
        z.pop() 

print("Result:", z[0])

# 8074009147