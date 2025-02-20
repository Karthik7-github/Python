a = int(input("enter a no  : "))

b = []

for i in range(a):
    b.append(int(input(f"Enter number {i+1}: ")))

b.reverse()

print(b)

