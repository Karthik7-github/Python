a = input()
b = []

for i in a:
    if i.isdigit():  # Check if the character is a digit
        b.append(int(i))

c = []
for i in b :
    sum = 0
    while i>0:
            rem = i%10
            sum = sum+rem
            i = i/1         
    c.append(int(sum))    

print(c)     