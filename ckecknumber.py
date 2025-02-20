print("enter the values:")
a = list(map(int,input().split()))
x=1
while x==1:
     print("enter no to check :")
     b = int(input())
     print(f"{a.count(b)} times coured")
     print("enter 1 to continue or else 0 :")
     x = int(input())

