matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
s=0
for i in matrix:
    k=max(i)
    if matrix[i]!= matrix[-1]:
        print(f'{max(i)}+')
        s=s+k
    else:
        print(f'{max(-1)=}')
        s=s+k

print(s)

