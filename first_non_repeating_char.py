n=input().lower()
for i in n:
    if n.count(i)==1:
        print(f'first_non_repeating_char: {i}')
        break

