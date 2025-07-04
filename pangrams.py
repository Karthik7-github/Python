n=input().lower()
a=[]

for i in n:
    if i not in a:
        a.append(i)

if len(a)==26:
    print("pangram")
else:
    print("not pangram")
