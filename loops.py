# n=int(input())
# i=n
# while i>1:
#     print(i)
#     i=i/2

def isPrime(n):
    c=0
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n = int(input())
