n = input().lower()
a=[]

for i in n:
    if i not in a:
        a.append(i)
b=('abcdefghijklmnopqrstuvwxyz')

for i in b:
    if i not in a:
        a.append(i)

print(f'convert_itto_pangram: {a}')
