n=int(input("enter a number : "))
a=[]
for i in range(n):
    a.append(int(input(f'Enter a number {i+1}: ')))

c=0
if n%2==0:
    k=n//2
else:
    k=(n//2)+1

for i in range(0,k,1):
    if a[i] == a[n-i-1]:
        c=c+1

if c == k:
    print('List is palindrome')
else:
    print('List is not palindrome')


# n = int(input("Enter the number of elements: "))
# a = []

# for i in range(n):
#     a.append(int(input(f'Enter a number {i+1}: ')))

# # Check if the list is a palindrome
# if a == a[::-1]:  # Compare the list with its reverse
#     print('List is palindrome')
# else:
#     print('List is not palindrome')