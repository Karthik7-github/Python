n = input('Enter a string: ').lower()

for i in n:
    c=0
    for j in n:
        if i == j:
            c=c+1
    print(f'The character {i} occurs {c} times')

