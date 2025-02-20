a = int(input("enter a no  : "))

b = []
for i in range(0,a,1):
    b.append(int(input(f"enter a {i+1} no ")))
for i in range(0,a,1):
    print(b[i])

c = int(input("enter  a no to add : "))    
b.append(c)
print(b)