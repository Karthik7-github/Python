k = input()
dict = {}
for i in k:
    a = k.count(i)
    dict[i] = a
for i in sorted(dict):
    print(f"{i} : {dict[{i}]}")