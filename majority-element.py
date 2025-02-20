a = int(input("enter a ele : "))

b = []
for i in range(a):
    b.append(int(input(f"enter ele {i+1} ;")))
c = []

for i in range(a):
    d = 0
    for j in range(a):
     if(b[i]==b[j]):
        c[i] = d+1

j = i + 1  

for i in range(a):
    max = c[i]
    for j in range(a):
       if(max>c[j]):
          temp = max
          max = c[j]
          c[j] = temp
print(max)          