def prime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
        else:
            return True

def next_prime(n):
    next_num = n+1
    while True:
        if prime(next_num):
            return next_num
        next_num +=1

num = int(input())
print(next_prime(num))