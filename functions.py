# def sum( n):
#     return n;
# def msg():
#     print("it is working !")
# a = int(input())
# print(sum(a))
# msg()
# print(msg())

# def changeitem(items):
#     items[2] = 50
# numbers = [10,20,30]
# changeitem(numbers)
# print(numbers)

# def modify(items):
#     items=[20,30,40]
#     return items
# numbers = [10,60,70]
# modify(numbers)
# print(numbers)

# def dum():
#     print("hi")
# dum()

# def sum():
#     print("hello")
# sum(9)

# def ages(age = 20):
#     print(age)
# ages(30)
# ages()


#lambda fun
# sum = lambda x,y : x**y
# print(sum(8,9))

# a = list(map(int,input().split()))
# b = list(map(lambda x:x+x,a))
# print(*b)

# def sqr(x):
#     return x**2
# a = [1,2]
# b = list(map(sqr,a))

#enumerate fun
# a = list(map(int,input().split()))
# b = list(enumerate(a,100))
# for i in b:
#     print(i)
#output:
# 1 2 3
# (100, 1)
# (101, 2)
# (102, 3)  

#zip fun
# c=[1,2,3]
# v=("a","b","c")
# r=list(zip(c,v))
# print(r)
# a,b=zip(*r)
# print("c -> ",a)
# print("v -> ",b)
# output : 
# [(1, 'a'), (2, 'b'), (3, 'c')]
# c ->  (1, 2, 3)
# v ->  ('a', 'b', 'c')

#reduce fun
# import functools
# l = [1,2,3,4]
# def mul(x,y):
#     return x*y;
# product = functools.reduce(mul,l)
# print(product)


# b= 200
# def fun():
#     b=10
#     print(b)
#     print(globals()['b'])
# fun()
# output :
# 10
# 200


#docs
# b = 900
# def fun():
#     '''
#     This is a doc
#     '''
#     b=10
#     print(b)
#     print(globals()['b'])

# print(fun.__doc__)
