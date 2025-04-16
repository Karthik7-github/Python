# print("Enter a num : ")
# a = 45
# b = 6
# c = 89
# d = 12
# print(a+b+c+d)
# print(a*b*c*d)
# print((c+b)-(a+d)+20)
# print(c-a)

# print(a+b+c+d)
# print(a+b+(c//d))
# print(a+c-(d-b))
# print(a*b*c*d)

n= int(input("enter a number : "))
x=n
sum=0
for i in range(1,n+1):
    p=pow(x,i)
    s=s+p
    if(i!=x):
        print("pow(x,",i,")+",end="")
    else:
        print("pow(x,",i,")+",end="\n")

print(s)

