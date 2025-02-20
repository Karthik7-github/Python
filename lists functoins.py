# x = [1,2,3,4,5,6,7]
# a = x[:]
# print(a)

# for i in a :
#       print(i,end=" ")
#       s=s+i

#append
# a.append(90)
# print(a)
# #insert
# a.insert(3,100)
# print(a)
# #pop
# a.pop(4)
# print(a)
# #remove
# a.remove(100)
# print(a)
# #extend
# b = [10,20]
# a.extend(b)
# print(a)
# #sort
# b = a
# a.sort()
# print(a)#asc


a=int(input())
b=int(input())
l=[]
c=[]
for i in range(a,b+1):
    if i%2==0:
        l.append(i)
for i in range(b,a-1,-1):
    if i%2!=0:
        c.append(i)
d=[]
c=1
for i in range(a,b+1):
    if c==1:
        X=l.pop(0)
        d.append(x)
        c=2
    else:
        x=c.pop(0)
        d.append(x)
        c=1

print(d)