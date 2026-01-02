# n=int(input("enter no of numbers u want : "))
# x=0
# y=1
# while(n>0):
#     z=y+x
#     x=y
#     y=z
#     n=n-1
# print(z)

# Input


n = int(input("Enter size: "))
a = list(map(int, input("Enter elements: ").split()))

def check(c):
    # c = 1 -> start with >
    # c = 0 -> start with <
    for i in range(1, len(a)):
        if c == 1:   # expecting >
            if a[i-1] <= a[i]:
                return False
        else:        # expecting <
            if a[i-1] >= a[i]:
                return False
        c = 1 - c   # flip expectation (0->1, 1->0)
    return True

# Decide start pattern
if a[0] > a[1]:
    c = 1
else:
    c = 0

print(check(c))
