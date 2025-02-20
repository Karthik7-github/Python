import math
a = int(input())
b = int(input())
c = int(input())
x = (a,b,c)

d = int(input())
e = int(input())
f = int(input())
y =(d,e,f)

print(x,y)
#Hint: Represent a ball on a plane as a tuple of (x, y, r), r being the radius.
#If (distance between two balls centers) <= (sum of their radii) then (they are colliding)

distance = math.sqrt((a-b)**2+(d-e)**2)
if distance<=(c+f):
    print(True)
else:
    print(False)