n=int(input("Enter the number of elements: "))
a=[]
for i in range(n):
    a.append(int(input(f'Enter a number {i+1}: ')))

i = 0
while i < len(a):
    j = i + 1
    while j < len(a):
        if a[i] == a[j]:
            a.pop(j)  # Remove the duplicate
        else:
            j += 1  # Only increment if no duplicate is removed
    i += 1  # Move to the next element

print('The list after removing duplicates is:', a)
