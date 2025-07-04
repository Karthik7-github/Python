n=input().lower()
a=[]
for i in n:
        if i not in a:
            a.append(i)
            print(f'{i}: {n.count(i)}')
        