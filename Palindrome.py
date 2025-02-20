x= int(input())
a = str(x)
c = int(a[::-1])
if x==c:
    print("Palindrome")
else:
    print("NOT")
