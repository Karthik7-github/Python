n = int(input("Enter the number of elements: "))
a = []
b=[]
for i in range(n):
    a.append(int(input("Enter the number: ")))
for i in a:
    num = i
    k=i%10
    found=-1
    while i>0:
        rem=i%10
        i=i//10
        if rem!=k:
            found=-1
            break
        else:
            found=1
    if found==1:
        b.append(num)
print(b)
