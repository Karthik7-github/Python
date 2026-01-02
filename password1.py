s=input()
sp=0
cp=0
d=0
n=len(s)
if n>8 and n<15:
    for i in s:
        if i in '0987654321':
            d=d+1
        elif ord(i)>=97 and ord(i)<=122:
            continue
        elif ord(i)>=65 and ord(i)<=90:
            cp=cp+1
        else:
            sp=sp+1
    if sp>=3 and cp>=3 and d>=2 :
        print("Valid")
    else:
        print("Not Valid")
else:
    print("Not Valid")
