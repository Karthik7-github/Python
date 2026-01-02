s=input()
c=0
a="abcdefghijklmnopqrstuvwxyz"
for i in a:
    if i not in s:
        # print("not")
        # c=1
        # break
# if c==0:
#     print("Pangram")
       s=s+i
print(s)
