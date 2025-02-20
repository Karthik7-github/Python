from math import sqrt
print("enter first point x,y,z : ")
x = [int(x) for x in input().split()]
print("Enter second point x,y,z : ")
y = [int(x) for x in input().split()]
dist = sqrt((y[1]-x[1])**2 + (y[0]-x[0])**2)
if dist <= x[2]+y[2]:
    print("Not Colliding")
else:
    print("Colliding")