n = int(input("enter no of numbers : "))
a=[]
b=[]
print("enter the first list of numbers")
for i in range(n):
    a.append(int(input("enter the number : ")))
print("enter the second list of numbers")

target = int(input("enter the target number : "))
found = False
for i in range(n):
    for j in range(n):
        if a[i] + a[j] == target:
            found = True
            print(f"found {a[i]} + {a[j]} = {target}")
            print(f" {i} and {j}")
            break
    if found:
        break
if not found:
    print("not found")

