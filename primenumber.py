x = int(input())#10


a = []
for i in range(x+1,x+100): # 11 to 109
    c = 0
    for j in range(2,i): # 2 to 10
        if i%j==0 :
             c = c+1
    if c==0 :
        a.append(i)

        
print(a[0])