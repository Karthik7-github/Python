n = input("Enter a value : ").lower()
found = True
for i in range(0,len(n)//2):
    if n[i] == n[len(n)-i-1]:
        found = True
    else:
        found = False
        break

print("The string is a palindrome") if found else print("The string is not a palindrome")