n = input("Enter a value : ").lower()
a=0
b=0
for i in n:
    if i in ['a','e','i','o','u']:
         a+=1
    else:
        b+=1

print("Number of vowels in the string is : ",a)
print("Number of consonants in the string is : ",b)

